from datetime import datetime

from pydantic import BaseModel, Field

class RequestAddConsultation(BaseModel):
    client_name: str
    client_number: str
    client_car: str
    client_comment: str | None = Field(None)

class Consultation(RequestAddConsultation):
    id: int
    status: str = "new"
    created_at: datetime
    order_type: str
    price: None = None
    ids_service_details: None = None

class AddConsultation(RequestAddConsultation):
    order_type: str = Field(default="consultation")


class PATCHConsultation(BaseModel):
    client_name: str | None = Field(default=None)
    client_number: str | None = Field(default=None)
    client_car: str | None = Field(default=None)
    client_comment: str | None = Field(default=None)
    status: str | None = Field(default=None)