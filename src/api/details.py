from fastapi import APIRouter
from src.database import async_session_maker
from sqlalchemy import select
from src.models.details import DetailsORM

router = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router.get('')
async def get_details(
        id: int
):
    async with async_session_maker() as session:
        result = await session.execute(select(DetailsORM).where(id==id))
        return result.scalars().all()