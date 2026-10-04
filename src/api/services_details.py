from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.services_details import RequestAddServiceDetail, PATCHServiceDetail


router = APIRouter(
    prefix="/prices",
    tags = ["Цены"]
)

@router.get("")
async def get_all_prices(
        db: DBDep,
):
    result = await db.services_details.get_all()
    return result

@router.post("")
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

@router.put("/{price_id}")
async def full_update_price(
        db: DBDep,
        price_id: int,
        data: RequestAddServiceDetail
):
    await db.services_details.edit(data=data, id=price_id)
    await db.commit()
    return {"status": "OK"}

@router.patch("/{price_id}")
async def partially_update_price(
        db: DBDep,
        price_id: int,
        data: PATCHServiceDetail
):
    await db.services_details.edit(data=data, is_patch=True, id=price_id)
    await db.commit()
    return {"status": "OK"}

@router.delete("/{price_id}")
async def delete_price(
        db: DBDep,
        price_id: int
):
    await db.services_details.delete(id=price_id)
    await db.commit()
    return {"status": "OK"}