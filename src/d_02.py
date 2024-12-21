from fastapi import FastAPI
from src.services.item import Item
import uvicorn

app = FastAPI()

db_time_entries = [
    {"id": 1, "description": "Meeting with the team", "duration": "10.44"},
    {
        "id": 2,
        "description": "Modelling 375Street with materials and textures to be included later",
        "duration": "12.98",
    },
    {
        "id": 3,
        "description": "Code review",
        "duration": "15.78",
    },
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/entries/")
async def read_entries():
    return db_time_entries


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item, q: str = None):
    return {"data": item, "q": q}


def day_two():
    print("\nDAY TWO IS ROLLING!")
    uvicorn.run(app, host="localhost", port=8000)