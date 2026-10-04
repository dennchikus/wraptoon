from pydantic import BaseModel, Field

class RequestAddService(BaseModel): # получение данных от пользователя(дургой разраб/заказчик)
    name_service: str

class Service(RequestAddService): # схема по которой данные отдаются пользователю
    id: int
