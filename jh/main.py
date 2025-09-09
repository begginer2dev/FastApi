from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = None

Items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}

@app.get("/item")
def read_items():
    return Items

@app.post("/item")
def create_item(item: Item):
    Items.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):    
    for item in Items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}  

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(item):
        if item.id == item_id:
            item[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(item):
        if item.id == item_id:
            deleted = item.pop(index)
            return deleted
    return {"error": "Item not found"}
