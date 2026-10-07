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

class ReadableServiceDetails(BaseModel):
    id: int
    name_service: str
    name_detail: str
    price: int
