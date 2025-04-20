from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List 

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    origin: str

itemList: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/itemList")
def get_item_list():
    return itemList

@app.post("/itemList")
def add_item(item: Item):
    itemList.append(item)
    return {"message": "Item added successfully: ", "item": item}
            
@app.put("/itemList/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(itemList):
        if item.id == item_id:
            itemList[index] = updated_item
            return {"messaege": "Item updated successfully", "item": updated_item}
    return {"message": "Item not found"}
    
@app.delete("itemList/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(itemList):
        if item.id == item_id:
            deleted = itemList.pop(index)
            return {"messaege": "Item deleted successfully", "item": deleted}
    return {"message": "Item not found"}

