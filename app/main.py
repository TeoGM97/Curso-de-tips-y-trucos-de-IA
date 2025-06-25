from fastapi import FastAPI
from app.routers import items

app = FastAPI(
    title="Mi API con FastAPI",
    description="API de ejemplo creada con FastAPI",
    version="0.1.0"
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a mi API con FastAPI!"} 