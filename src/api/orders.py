from fastapi import APIRouter, BackgroundTasks

from src.api.dependencies import DBDep, AdminDep
from src.schemas.orders import RequestAddOrder, PATCHOrder, AddOrder
from src.services.tg_notification_bot import send_notification_tg, TemplatesMessages

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
        data: RequestAddOrder,
        background_tasks: BackgroundTasks
):
    price = 0
    items = []
    if data.ids_service_details is not None:
        ids = list(data.ids_service_details.keys())
        model = await db.services_details.get_readable_all_relationships(ids=ids)
        for item in model:
            item_quantity = data.ids_service_details[item.id]
            price += item_quantity * item.price
            formated_price_single_item = f"{item.price * item_quantity:,}".replace(",", " ")
            items.append(f"• {item.name_detail} ({item.name_service}) - {item_quantity} шт. - {formated_price_single_item} ₽")

    _data = AddOrder(order_type="calculator", price=price, **data.model_dump())
    result = await db.orders.add(data=_data)
    await db.commit()



    tg_message_text = TemplatesMessages.order_message(
        client_name=data.client_name,
        client_number=data.client_number,
        client_car=data.client_car,
        client_comment=data.client_comment,
        price=price,
        items=items
    )

    background_tasks.add_task(send_notification_tg, text=tg_message_text)

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