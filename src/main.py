import uvicorn
from fastapi import FastAPI

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.api.calc import router as router_calc

app = FastAPI()

app.include_router(router_calc)

@app.get("/")
def hello(name: str):
    name = name
    return {"hello": name}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)