from fastapi import APIRouter

from src.api.dependencies import DBDep, AdminDep
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
        db: DBDep,
        _: AdminDep,
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
    price = 0
    if data.ids_service_details is not None:
        ids = (data.ids_service_details.keys())
        for i in ids:
            service_detail = await db.services_details.get_one_or_none(id=i)
            price += service_detail.price * data.ids_service_details[i]

    _data = AddOrder(order_type="calculator", price=price, **data.model_dump())
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
        _: AdminDep,
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
        _: AdminDep,
        order_id: int,
):

    await db.orders.delete(id=order_id)
    await db.commit()
    return {"status": "OK"}