from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(item, q: str = None):
    print(item, q)
    return item


def day_two():
    print("\nDAY TWO IS ROLLING!")
    uvicorn.run(app, host="localhost", port=8000)