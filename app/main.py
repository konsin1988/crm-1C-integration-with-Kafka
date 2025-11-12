from fastapi import FastAPI, status, Request
from fastapi.responses import HTMLResponse, JSONResponse
import pandas as pd
import datetime
from dotenv import load_dotenv
import os
import cryptography
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from core.config import settings
from utils.appException import AppException

from core.kafka import init_kafka_producer, close_kafka_producer


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix="/api")

origins = ["http://localhost:3000", "http://test.rtt.digital", "https://test.rtt.digital", "https://sima.rtt.digital"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_kafka_producer()

@app.on_event("shutdown")
async def shutdown_event():
    await close_kafka_producer()

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
            status_code=exc.code,
            content={"error": exc.message}
            )


@app.get('/')
def health(request: Request):
    return JSONResponse(status_code=200, content={"health": "ok"}) 
