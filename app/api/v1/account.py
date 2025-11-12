from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from db.session import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from crud import account
from utils.appException import AppException
from services.producer import send_to_kafka

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/{id}")
async def get_car_data(id: int, db: AsyncSession = Depends(get_db)):
    data = await account.get_car_data(db, id)
    if not data:
        return {"error": "Car not found"}

    await send_to_kafka(data)
    #return data

