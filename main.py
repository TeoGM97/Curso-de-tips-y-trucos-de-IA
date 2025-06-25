from fastapi import FastAPI

app = FastAPI(
    title="Mi API con FastAPI",
    description="API de ejemplo creada con FastAPI",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a mi API con FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id} 