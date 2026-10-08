# Библиотеки
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Починка путей
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# Роутеры
from src.api.details import router as router_details
from src.api.services import router as router_services
from src.api.services_details import router as router_services_details
from src.api.orders import router as router_orders
from src.api.consultations import router as router_consultation

from src.config import settings
app = FastAPI(
    docs_url="/docs" if settings.MODE == "DEV" else None,
    redoc_url="/redoc" if settings.MODE == "DEV" else None,
    openapi_url="/openapi.json" if settings.MODE == "DEV" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://127.0.0.1:{settings.FRONTEND_PORT}",
        f"http://localhost:{settings.FRONTEND_PORT}"
    ],
    allow_credentials=True,
    allow_methods=["*"],            # Разрешаем все методы (GET, POST, PATCH и т.д.)
    allow_headers=["*"],
)

app.include_router(router_details)
app.include_router(router_services)
app.include_router(router_services_details)
app.include_router(router_orders)
app.include_router(router_consultation)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
