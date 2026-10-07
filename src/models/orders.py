from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

from src.database import Base

class OrdersORM(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str] = mapped_column(String(length=50))
    client_number: Mapped[str] = mapped_column(String(length=20))
    client_car: Mapped[str] = mapped_column(String(length=50))
    client_comment: Mapped[str | None] = mapped_column(String(length=500), nullable=True)
    price: Mapped[int | None] = mapped_column(nullable=True)
    ids_service_details: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    order_type: Mapped[str] = mapped_column(String(length=15))
    status: Mapped[str] = mapped_column(String, default="new")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())