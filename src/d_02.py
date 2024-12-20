from fastapi import FastAPI
from src.services.item import Item
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item:Item, q: str = None):
    return {"data": item, "q": q}


def day_two():
    print("\nDAY TWO IS ROLLING!")
    uvicorn.run(app, host="localhost", port=8000)