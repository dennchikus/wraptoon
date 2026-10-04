from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class ServicesORM(Base):
    __tablename__ = "services"

    id:Mapped[int] = mapped_column(primary_key=True)
    name_service:Mapped[str] = mapped_column(String(length=30))
    