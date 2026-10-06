from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.orders import RequestAddOrder, PATCHOrder, AddOrder

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
    return await db.orders.get_filtered(order_type="calculator")

@router.post(
    "",
    summary="Добавить новый заказ",
    description="Добавление нового заказа в перечень"
)
async def add_order(
        db: DBDep,
        data: RequestAddOrder
):
    _data = AddOrder(order_type="calculator", **data.model_dump())
    result = await db.orders.add(data=_data)
    await db.commit()

    return {
        "status": "OK",
        "data": result
    }

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