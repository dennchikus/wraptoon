from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


from src.database import Base


class DetailsORM(Base):
    __tablename__ = "details"

    id:Mapped[int] = mapped_column(primary_key=True)
    name_detail:Mapped[str] = mapped_column(String(length=40))
