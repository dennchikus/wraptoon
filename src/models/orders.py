from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.database import Base

class OrdersORM(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str] = mapped_column(String(length=50))
    client_number: Mapped[str] = mapped_column(String(length=20))
    client_car: Mapped[str] = mapped_column(String(length=50))
    client_comment: Mapped[str] = mapped_column(String(length=500), nullable=True)
    price: Mapped[int]
    ids_service_details: Mapped[str] = mapped_column(String(length=100))
    status: Mapped[str] = mapped_column(String, default="new")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())