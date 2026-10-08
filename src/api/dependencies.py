from typing import Annotated
import secrets

from fastapi import Depends, Header, HTTPException, status

from src.database import async_session_maker
from src.utils.db_manager import DBManager

from src.config import settings

def get_db_manager():
    return DBManager(session_factory=async_session_maker)

async def get_db():
    async with get_db_manager() as db:
        yield db

DBDep = Annotated[DBManager, Depends(get_db)]

def verify_admin_token(
    x_admin_token: Annotated[str | None, Header(alias="X-Admin-Token")] = None
):
    if not x_admin_token or not secrets.compare_digest(x_admin_token, settings.SECRET_ADMIN_TOKEN):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Доступ запрещен: неверный или отсутствует X-Admin-Token"
        )

AdminDep = Annotated[None, Depends(verify_admin_token)]
