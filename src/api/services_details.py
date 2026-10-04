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
    return {
        "status": "OK",
        "data": result
    }

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

@router.put("/{id_price}")
async def full_update_price(
        db: DBDep,
        id_price: int,
        data: RequestAddServiceDetail
):
    await db.services_details.edit(data=data, id=id_price)
    await db.commit()
    return {"status": "OK"}

@router.patch("/{id_price}")
async def partially_update_price(
        db: DBDep,
        id_price: int,
        data: PATCHServiceDetail
):
    await db.services_details.edit(data=data, is_patch=True, id=id_price)
    await db.commit()
    return {"status": "OK"}

@router.delete("/{id_price}")
async def delete_price(
        db: DBDep,
        id_price: int
):
    await db.services_details.delete(id=id_price)
    await db.commit()
    return {"status": "OK"}