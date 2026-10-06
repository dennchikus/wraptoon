# Библиотеки
import uvicorn
from fastapi import FastAPI

# Починка путей
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# Роутеры
from src.api.details import router as router_details
from src.api.services import router as router_services
from src.api.services_details import router as router_services_details
from src.api.orders import router as router_orders

app = FastAPI()

app.include_router(router_details)
app.include_router(router_services)
app.include_router(router_services_details)
app.include_router(router_orders)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)