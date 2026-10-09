from fastapi import APIRouter, BackgroundTasks

from src.schemas.consultations import RequestAddConsultation, AddConsultation, PATCHConsultation
from src.api.dependencies import DBDep, AdminDep
from src.services.tg_notification_bot import send_notification_tg, TemplatesMessages

router = APIRouter(
    prefix="/consultations",
    tags=["Консультации"]
)

@router.get(
    "",
    summary="Получить список записей на консультацию",
    description="Выводится перечень записей на консультацию"
)
async def get_all_consultations(
        db: DBDep,
        _:AdminDep
):

    return await db.orders.get_filtered(order_type="consultation")

@router.post(
    "",
    summary="Добавление новой записи на консультацию",
    description="Создает новую запись консультации в перечне"
)
async def add_consultation(
        db: DBDep,
        data: RequestAddConsultation,
        background_tasks: BackgroundTasks
):
    _data = AddConsultation(order_type="consultation", **data.model_dump())
    result = await db.orders.add(data=_data)
    await db.commit()

    tg_message_text = TemplatesMessages.consultation_message(
        client_name=data.client_name,
        client_number=data.client_number,
        client_car=data.client_car,
        client_comment=data.client_comment
    )

    background_tasks.add_task(send_notification_tg, text=tg_message_text)

    return {
        "status": "OK",
        "data": result
    }

@router.patch(
    "/{consultation_id}",
    summary="Изменение данных записи по идентификатору",
    description="Корректировка данных клиента по идентификатору его записи в перечне"
)
async def partially_edit_consultation(
        db: DBDep,
        _:AdminDep,
        consultation_id: int,
        data: PATCHConsultation
):
    await db.orders.edit(data=data, is_patch=True, id=consultation_id)
    await db.commit()
    return {"status": "OK"}

@router.delete(
    "/{consultation_id}",
    summary="Удаление записи из перечня",
    description="Полностью удаляет запись на консультацию из перечня по ее идентификатору"
)
async def delete_consultation(
        db: DBDep,
        _: AdminDep,
        consultation_id: int,
):

    await db.orders.delete(id=consultation_id)
    await db.commit()
    return {"status": "OK"}