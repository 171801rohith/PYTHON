from fastapi import FastAPI, Path, Query, status, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {}


@app.get("/")
def home():
    return {"Data": "FastAPI is cool"}


@app.get("/about")
def about():
    return {"Data": "About us"}


# EndPoint Parameter
# @app.get("/get-item/{item_id}/{name}")
# def get_item_name(item_id: int, name: str):
#         inventory_item = inventory[item_id]
#         print(inventory_item)
#         return inventory_item[name]


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="ID can be a INTEGER", lt=3, gt=0)):
    return inventory[item_id]


# Query Parameter
@app.get("/get-by-name")
def get_itemName(name: Optional[str] = Query(None, description="Item name")):
    # OR
    # def get_item_name(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found in Inventory")


# EndPoint and Query Together
@app.get("/get-by-name/{item_id}")
def get_item_name(*, test: int, name: Optional[str] = None, item_id: int):
    if inventory[item_id].name == name:
        return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found in Inventory")



@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item already exists in Inventory")

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found in Inventory")

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="Id of item to be deleted", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found in Inventory")
    
    del inventory[item_id]
