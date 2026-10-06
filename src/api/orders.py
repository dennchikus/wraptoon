from fastapi import APIRouter, Query

from src.api.dependencies import DBDep
from src.schemas.orders import RequestAddOrder, PATCHOrder

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"]
)

@router.get(
    "",
    summary="Получить список заказов",
    description="Возвращает перечень всех заказов"
)

async def get_all_orders(
        db: DBDep
):
    return await db.orders.get_all()

@router.post(
    "",
    summary="Добавить новый заказ",
    description="Добавление нового заказа в перечень"
)

async def add_order(
        db: DBDep,
        data: RequestAddOrder
):
    result = await db.orders.add(data=data)
    await db.commit()

    return {
        "status": "OK",
        "data": result
    }

@router.put(
    "/{order_id}",
    summary="Полное изменение данных заказа",
    description="Полностью перезаписывает информацию о заказе по его идентификатору"
)

async def full_update_order(
        db: DBDep,
        order_id: int,
        data: RequestAddOrder
):
    await db.orders.edit(id=order_id, data=data)
    await db.commit()

    return {"status": "OK"}

@router.patch(
    "/{order_id}",
    summary="Частичное изменение данных заказа",
    description="Позволяет частично скорректировать информацию о заказе по его идентификатору"
)

async def partially_update_order(
    db: DBDep,
    order_id: int,
    data: PATCHOrder
):
    await db.orders.edit(data=data, is_patch=True, id=order_id)
    await db.commit()
    return {"status": "OK"}

@router.delete(
    "/{order_id}",
    summary="Удаление заказа из перечня",
    description="Полностью удаляет заказ из списка"
)

async def delete_order(
        db: DBDep,
        order_id: int,
):

    await db.orders.delete(id=order_id)
    await db.commit()
    return {"status": "OK"}