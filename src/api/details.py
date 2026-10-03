from fastapi import APIRouter, HTTPException, Query

from src.api.dependencies import DBDep
from src.schemas.details import RequestAddDetails, PATCHDetails

router = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router.get("")
async def get_details_by_name(
        db: DBDep,
        name_detail: str | None = Query(None),
):
    return await db.details.get_filtered_by_name(name_detail=name_detail)

@router.post("")
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

@router.put("/{detail_id}")
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

@router.patch("/{detail_id}")
async def partially_update_detail(
        db: DBDep,
        detail_id: int,
        data: PATCHDetails
):
    _data = data.model_dump(exclude_unset=True)
    if not _data:
        raise HTTPException(status_code=400, detail="Bad Request")
    await db.details.edit(data=data, id=detail_id, is_patch=True)
    await db.commit()
    return {
        "status": "OK",
    }

@router.delete("/{detail_id}")
async def delete_detail_by_id(
        db: DBDep,
        detail_id: int
):
    await db.details.delete(id=detail_id)
    await db.commit()
    return {
        "status": "OK"
    }