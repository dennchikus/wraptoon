from datetime import datetime

from pydantic import BaseModel, Field

class RequestAddOrder(BaseModel):
    client_name: str
    client_number: str
    client_car: str
    client_comment: str | None = Field(None)
    ids_service_details: str | None = Field(None)

class Order(RequestAddOrder):
    id: int
    price: int | None = None
    status: str = "new"
    created_at: datetime
    order_type: str

class AddOrder(RequestAddOrder):
    order_type: str = Field(default="calculator")

class PATCHOrder(BaseModel):
    client_name: str | None = Field(default=None)
    client_number: str | None = Field(default=None)
    client_car: str | None = Field(default=None)
    client_comment: str | None = Field(default=None)
    price: int | None = Field(default=None)
    ids_service_details: str | None = Field(default=None)
    status: str | None = Field(default=None)