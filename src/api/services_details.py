from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.services_details import RequestAddServiceDetail, PATCHServiceDetail


router = APIRouter(
    prefix="/prices",
    tags = ["Цены"]
)

@router.get(
    "",
    summary="Получить все связки услуг и деталей",
    description="Возвращает перечень установленных соответствий между услугами и деталями с указанием их цен"
)
async def get_all_prices(
        db: DBDep,
):
    result = await db.services_details.get_readable_all_relationships()
    return result

@router.post(
    "",
    summary="Добавить соответствие детали и услуги",
    description="Создает новую запись соответствия: закрепляет деталь за выбранной услугой и фиксирует стоимость"
)
async def add_price(
        db: DBDep,
        data: RequestAddServiceDetail
):
    result = await db.services_details.add(data=data)
    await db.commit()
    return {
        "status" : "OK",
        "data": result
    }

@router.put(
    "/{price_id}",
    summary="Полностью обновить связь детали и услуги",
    description="Полная перезапись параметров привязки"
                "замена идентификаторов детали и услуги, а также изменение цены по идентификатору связки"
)
async def full_update_price(
        db: DBDep,
        price_id: int,
        data: RequestAddServiceDetail
):
    await db.services_details.edit(data=data, id=price_id)
    await db.commit()
    return {"status": "OK"}

@router.patch(
    "/{price_id}",
    summary="Частично обновить связь",
    description="Позволяет скорректировать цену или перепривязать услугу/деталь без передачи всех параметров по идентификатору связки"
)
async def partially_update_price(
        db: DBDep,
        price_id: int,
        data: PATCHServiceDetail
):
    await db.services_details.edit(data=data, is_patch=True, id=price_id)
    await db.commit()
    return {"status": "OK"}

@router.delete(
    "/{price_id}",
    summary="Удаление связки",
    description="Полностью удаляет запись связки по ее идентификатору, отвязывая деталь от услуги и удаляя цену"
)
async def delete_price(
        db: DBDep,
        price_id: int
):
    await db.services_details.delete(id=price_id)
    await db.commit()
    return {"status": "OK"}