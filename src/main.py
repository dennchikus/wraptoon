import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello(name: str):
    name = name
    return {"hello": name}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)