from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/calc",
    tags=["Калькулятор"]
)

details = {
    "Капот": 17000,
    "Фары": 4000
    ,"Передний бампер": 18000
    ,"Стойки": 2000
}

@router.post(
    "",
    summary="Основной калькулятор стоимости",
    description="Эндпоинт, расчитывающий общую стоимость оклейки"
)
def calc(
        kapot: int = Body(default=0),
        fari: int = Body(default=0),
        bumper: int = Body(default=0),
        stoyki: int = Body(default=0)
):
    result = kapot*details["Капот"]+fari*details["Фары"]+bumper*details["Передний бампер"]+stoyki*details["Стойки"]
    return {"Рассчетная стоимость": f"{result}P.",
            "status": "OK"}

# TODO Начать делать пайдентик схемы.