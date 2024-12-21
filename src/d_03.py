import requests
from services.time_entry import TimeEntry
from pprint import pprint


BASE_URL = "http://localhost:8000"

first_time_entry = TimeEntry(
    description="Designed the Engine with Quad-core processor and 16GB RAM",
    duration=10.45,
)

def get_item(item_id: int):
    ITEMS_URL = f"{BASE_URL}/items/{item_id}"
    response = requests.get(ITEMS_URL, params={"q": "This is a GET query"})
    data = response.json()
    pprint(data)
    return data


def post_item(item):
    ITEM_POST_URL = f"{BASE_URL}/items/"
    response = requests.post(ITEM_POST_URL, json=item, params={"q": "This is a POST query"})
    data = response.json()
    print(data)
    return data

get_item(3)
post_item(first_time_entry.__dict__)
