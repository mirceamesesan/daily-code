from fastapi import FastAPI
from .services.time_entry import TimeEntry
from typing import List
import uvicorn

app = FastAPI()

db_time_entries: List[dict] = [
    {
        "description": "Meeting with the team and short introductions", 
        "duration": "10.44"
    },
    {
        "description": "Modelling 375Street with materials and textures to be included later",
        "duration": "12.98",
    },
    {
        "description": "Code review",
        "duration": "15.78",
    },
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/entries/")
async def read_entries():
    print(f"Reading all entries... {len(db_time_entries)}")
    return db_time_entries


@app.post("/entry/")
async def create_item(entry: TimeEntry, q: str = None):
    db_time_entries.append(entry.make_dict())
    return read_entries()


def day_two():
    print("\nDAY TWO IS ROLLING!")
    uvicorn.run(app, host="localhost", port=8000)
