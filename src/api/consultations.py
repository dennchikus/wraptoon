from fastapi import APIRouter

from src.schemas.consultations import RequestAddConsultation, AddConsultation, PATCHConsultation
from src.api.dependencies import DBDep

router = APIRouter(
    prefix="/consultations",
    tags=["Консультации"]
)

@router.get("")
async def get_all_consultations(
        db: DBDep
):
    return await db.orders.get_filtered(order_type="consultation")

@router.post("")
async def add_consultation(
        db: DBDep,
        data: RequestAddConsultation
):
    _data = AddConsultation(order_type="consultation", **data.model_dump())
    result = await db.orders.add(data=_data)
    await db.commit()

    return {
        "status": "OK",
        "data": result
    }

@router.patch("/{consultation_id}")
async def partially_edit_consultation(
        db: DBDep,
        consultation_id: int,
        data: PATCHConsultation
):
    await db.orders.edit(data=data, is_patch=True, id=consultation_id)
    await db.commit()
    return {"status": "OK"}

@router.delete(
    "/{consultation_id}",
)
async def delete_order(
        db: DBDep,
        consultation_id: int,
):

    await db.orders.delete(id=consultation_id)
    await db.commit()
    return {"status": "OK"}