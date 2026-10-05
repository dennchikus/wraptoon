from fastapi import APIRouter, Query

from src.api.dependencies import DBDep
from src.schemas.services import RequestAddService

router = APIRouter(
    prefix="/services",
    tags=["Услуги"]
)

@router.get(
    "",
    summary="Получить список всех услуг",
    description="Возвращает каталог всех предоставляемых услуг"
)
async def get_services(
        db: DBDep,
):
    return await db.services.get_all()

@router.post(
    "",
    summary="Добавить новую услугу",
    description="Добавляет новую услугу в перечень предоставляемых услуг"
)
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

@router.put(
    "/{service_id}",
    summary="Обновить услугу",
    description="Полностью перезаписывает информацию об услуге по ее идентификатору"
)
async def full_update_service(
        db: DBDep,
        service_id: int,
        data: RequestAddService
):
    await db.services.edit(data=data, id=service_id)
    await db.commit()

    return {"status": "OK"}

@router.delete(
    "/{service_id}",
    summary="Удалить услугу",
    description="Удаляет позицию услуги из перечня по ее идентификатору"
)
async def delete_service(
        db: DBDep,
        service_id: int
):
    await db.services.delete(id=service_id)
    await db.commit()

    return{"status": "OK"}