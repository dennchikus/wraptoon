from fastapi import APIRouter, Query

from src.api.dependencies import DBDep
from src.schemas.services import RequestAddService

router = APIRouter(
    prefix="/services",
    tags=["Услуги"]
)

@router.get("")
async def get_services(
        db: DBDep,
):
    return await db.services.get_all()

@router.post("")
async def add_service(
        db: DBDep,
        data: RequestAddService
):
    result = await db.services.add(data=data)
    await db.commit()

    return {
        "status" : "OK",
        "data" : result
    }

@router.put("/{service_id}")
async def full_update_service(
        db: DBDep,
        service_id: int,
        data: RequestAddService
):
    await db.services.edit(data=data, id=service_id)
    await db.commit()

    return {"status": "OK"}

@router.delete("/{service_id}")
async def delete_service(
        db: DBDep,
        service_id: int
):
    await db.services.delete(id=service_id)
    await db.commit()

    return{"status": "OK"}