# Библиотеки
import uvicorn
from fastapi import FastAPI

# Починка путей
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

# Роутеры
from src.api.calc import router as router_calc

app = FastAPI()

app.include_router(router_calc)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)