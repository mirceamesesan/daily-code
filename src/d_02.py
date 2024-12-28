from fastapi import FastAPI
from .services.time_entry import TimeEntry
import uvicorn
from src.d_05 import SQLModel

app = FastAPI()
db = SQLModel()


@app.get("/entries/")
async def read_entries():
    entries = db.get_entries()
    return entries


@app.post("/entry/")
async def create_item(entry: TimeEntry, q: str = None):
    db.insert_entry(entry.project, entry.client, entry.description, entry.duration, entry.created_at)
    return read_entries()


@app.delete("/entry/{entry_id}")
async def delete_item(entry_id: int):
    db.remove_entry(entry_id)
    return read_entries()


def day_two():
    print("\nDAY TWO IS ROLLING!")
    uvicorn.run(app, host="localhost", port=8000)
