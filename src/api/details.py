from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import select, insert, update, delete

from src.repositories.details import DetailsRepository
from src.schemas.details import RequestAddDetails, PATCHDetails
from src.database import async_session_maker
from src.models.details import DetailsORM

router = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router.get("")
async def get_details_by_name(
        name_detail: str | None = Query(None),
):
    async with async_session_maker() as session:
        return await DetailsRepository(session).get_filtered_by_name(name_detail=name_detail)

@router.post("")
async def add_detail(
        data: RequestAddDetails
):
    async with async_session_maker() as session:
        result = await DetailsRepository(session).add(data)
        await session.commit()
        return {
            "status": "OK",
            "data": result
        }

@router.put("/{detail_id}")
async def full_update_detail(
        detail_id: int,
        data: RequestAddDetails
):
    async with async_session_maker() as session:
        await DetailsRepository(session).edit(data=data, id=detail_id)
        await session.commit()
        return {
            "status": "OK",
        }

@router.patch("/{detail_id}")
async def partially_update_detail(
        detail_id: int,
        data: PATCHDetails
):
    async with async_session_maker() as session:
        if data:
            print(data)
        else:
            print("data is clear")
        await DetailsRepository(session).edit(data=data, id=detail_id, is_patch=True)
        # if result is None:
        #     raise HTTPException(status_code=404, detail="Деталь не найдена")
        await session.commit()
        return {
            "status": "OK",
        }

@router.delete("/{detail_id}")
async def delete_detail_by_id(
        detail_id: int
):
    async with async_session_maker() as session:
        await DetailsRepository(session).delete(id=detail_id)
        await session.commit()
        return {
            "status": "OK"
        }