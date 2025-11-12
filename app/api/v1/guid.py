from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from db.session import SessionLocal

router = APIRouter()

@router.get("/")
async def get_guid(request: Request):
    return JSONResponse(content={"guid": "guid"})
