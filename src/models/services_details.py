from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class ServicesDetailsORM(Base):
    __tablename__ = "services_details"

    id:Mapped[int] = mapped_column(primary_key=True)
    service_id:Mapped[int] = mapped_column(ForeignKey("services.id"))
    detail_id:Mapped[int] = mapped_column(ForeignKey("details.id"))
    price:Mapped[int]