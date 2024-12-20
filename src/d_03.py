import requests
from services.item import Item
from pprint import pprint


BASE_URL = "http://localhost:8000"

first_item = Item(
    name="Peacock Engine XK2",
    description="Engine with Quad-core processor and 16GB RAM",
    price=130.45,
    tax=15.50,
)

def get_items(item_id: int):
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

get_items(3)
post_item(first_item.__dict__)
