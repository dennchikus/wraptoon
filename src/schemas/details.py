from pydantic import BaseModel, Field

class RequestAddDetails(BaseModel): # получение данных от пользователя(дургой разраб/заказчик)
    name_detail: str


class Details(RequestAddDetails): # схема по которой данные отдаются пользователю
    id: int


