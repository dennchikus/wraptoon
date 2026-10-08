from fastapi import APIRouter, HTTPException, Query, Depends

from src.api.dependencies import DBDep, verify_admin_token
from src.schemas.details import RequestAddDetails

router = APIRouter(
    prefix="/details",
    tags=["Детали"],
    dependencies=[Depends(verify_admin_token)]
)

@router.get(
    "",
    summary="Получить список всех деталей",
    description="Возвращает перечень всех зарегистрированных в системе деталей"
                "или перечень деталей, содержащих в названии введенное сочетание символов"
            )
async def get_details_by_name(
        db: DBDep,
        name_detail: str | None = Query(None),
):
    return await db.details.get_filtered_by_name(name_detail=name_detail)

@router.post(
    "",
    summary="Добавить новую деталь",
    description="Создает новую позицию по наименованию детали"
)
async def add_detail(
        db: DBDep,
        data: RequestAddDetails
):
    result = await db.details.add(data)
    await db.commit()
    return {
        "status": "OK",
        "data": result
    }

@router.put(
    "/{detail_id}",
    summary="Обновить данные детали",
    description="Полностью обновляет информацию о существующей детали по ее идентификатору"
)
async def full_update_detail(
        db: DBDep,
        detail_id: int,
        data: RequestAddDetails
):
    await db.details.edit(data=data, id=detail_id)
    await db.commit()
    return {
        "status": "OK",
    }

@router.delete(
    "/{detail_id}",
    summary="Удалить деталь",
    description="Удаляет запись детали по указанному идентификатору"
)
async def delete_detail_by_id(
        db: DBDep,
        detail_id: int
):
    await db.details.delete(id=detail_id)
    await db.commit()
    return {
        "status": "OK"
    }