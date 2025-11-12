import asyncio
from fastapi import FastAPI
from kafka.consumer_service import start_consumer
from db.db import init_db_pool, close_db_pool
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    app.state.db_pool = await init_db_pool()
    app.state.consumer_task = asyncio.create_task(start_consumer(app.state.db_pool))
    logger.info("Consumer started")

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_pool(app.state.db_pool)
    app.state.consumer_task.cancel()
    logger.info("Consumer stopped")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

