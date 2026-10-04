from pydantic import BaseModel, Field

class RequestAddServiceDetail(BaseModel):
    service_id: int
    detail_id: int
    price: int

class ServiceDetail(RequestAddServiceDetail):
    id: int

class PATCHServiceDetail(BaseModel):
    service_id: int | None = Field(default=None)
    detail_id: int | None = Field(default=None)
    price: int | None = Field(default=None)
