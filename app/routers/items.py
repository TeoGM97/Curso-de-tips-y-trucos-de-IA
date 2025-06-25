from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item no encontrado"}},
)

fake_items_db = {"1": {"name": "Laptop"}, "2": {"name": "Smartphone"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return fake_items_db[item_id] 