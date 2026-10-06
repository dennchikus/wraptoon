from pydantic import BaseModel, Field
from datetime import datetime

class RequestAddOrder(BaseModel):
    client_name: str
    client_number: str
    client_car: str
    client_comment: str | None = Field(None)
    price: int
    ids_service_details: str

class Order(RequestAddOrder):
    id: int
    status: str = "new"
    created_at: datetime

class PATCHOrder(BaseModel):
    client_name: str | None = Field(default=None)
    client_number: str | None = Field(default=None)
    client_car: str | None = Field(default=None)
    client_comment: str | None = Field(default=None)
    price: int | None = Field(default=None)
    ids_service_details: str | None = Field(default=None)
    status: str | None = Field(default=None)