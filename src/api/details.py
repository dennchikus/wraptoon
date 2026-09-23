from fastapi import APIRouter, Query

from schemas.details import RequestAddDetails, PATCHDetails
from src.database import async_session_maker
from sqlalchemy import select, insert, update, delete
from src.models.details import DetailsORM

router = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router.get("")
async def get_detail(
        detail_id: int = Query(default=None)
):
    async with async_session_maker() as session:
        query = select(DetailsORM)
        if detail_id is not None:
           query = query.filter_by(id=detail_id)
        result = await session.execute(query)
        return {
            "status": "OK",
            "data": result.scalars().all()
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

@router.put("")
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

@router.patch("")
async def full_update_detail(
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

@router.delete("")
async def delete_detail_by_id(
        detail_id: int
):
    async with async_session_maker() as session:
        result = await session.execute(delete(DetailsORM).filter_by(id=detail_id))
        await session.commit()
        return {"status": "OK"}