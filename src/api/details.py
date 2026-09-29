from fastapi import APIRouter, HTTPException

from schemas.details import RequestAddDetails, PATCHDetails
from src.database import async_session_maker
from sqlalchemy import select, insert, update, delete
from src.models.details import DetailsORM

router = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router.get("")
async def get_details():
    async with async_session_maker() as session:
        query = select(DetailsORM)
        result = await session.execute(query)
        return {"result": result.scalars().all()}

@router.get("/{detail_id}")
async def get_detail(
        detail_id: int
):
    async with async_session_maker() as session:
        query = select(DetailsORM).filter_by(id=detail_id)
        result = await session.execute(query)
        result = result.scalars().one_or_none()
        if result is None:
            raise HTTPException(status_code=404, detail="Detail not found!")
        return {
            "status": "OK",
            "data": result
        }

@router.post("")
async def add_detail(
        data: RequestAddDetails
):
    async with async_session_maker() as session:
        query = insert(DetailsORM).values(name_detail=data.name_detail, price=data.price).returning(DetailsORM)
        result = await session.execute(query)
        await session.commit()
        return {
            "status": "OK",
            "data": result.scalars().one()
        }

@router.put("/{detail_id}")
async def full_update_detail(
        detail_id: int,
        data: RequestAddDetails
):
    async with async_session_maker() as session:
        query = (
            update(DetailsORM)
            .filter_by(id=detail_id)
            .values(**data.model_dump())
            .returning(DetailsORM)
        )
        result = await session.execute(query)
        await session.commit()
        return {
            "status": "OK",
            "data": result.scalars().one()
        }

@router.patch("/{detail_id}")
async def partially_update_detail(
        detail_id: int,
        data: PATCHDetails
):
    async with async_session_maker() as session:
        query = (
            update(DetailsORM)
            .filter_by(id=detail_id)
            .values(**data.model_dump(exclude_unset=True))
            .returning(DetailsORM)
        )
        result = await session.execute(query)
        await session.commit()
        return {
            "status": "OK",
            "data": result.scalars().one()
        }

@router.delete("/{detail_id}")
async def delete_detail_by_id(
        detail_id: int
):
    async with async_session_maker() as session:
        result = await session.execute(delete(DetailsORM).filter_by(id=detail_id))
        await session.commit()
        return {"status": "OK"}