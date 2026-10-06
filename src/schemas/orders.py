from pydantic import BaseModel, Field
from datetime import datetime

class RequestAddOrders(BaseModel):
    client_name: str
    client_number: str
    client_car: str
    client_comment: str | None = None
    price: int
    id_service_details: int
    status: str = "New"

class Orders(RequestAddOrders):
    id: int
    created_at: datetime

class PATCHOrders(BaseModel):
    client_name: str | None = Field(default=None)
    client_number: str | None = Field(default=None)
    client_car: str | None = Field(default=None)
    client_comment: str | None = Field(default=None)
    price: int | None = Field(default=None)
    ids_service_details: str | None = Field(default=None)
    status: str | None = Field(default=None)