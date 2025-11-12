import asyncio
import json
from aiokafka import AIOKafkaConsumer
from core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def save_to_db(pool, data):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                    f"""update NomenclatureForm set car_guid = "{data['car_guid']}" where id = {data['id']}"""
                    )
        await conn.commit()

async def start_consumer(pool):
    consumer = AIOKafkaConsumer(
        settings.KAFKA_GUID_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    await consumer.start()
    logger.info("Kafka consumer connected..")

    try:
        async for msg in consumer:
            try:
                logger.info(f"Received: {msg.value}")
                await save_to_db(pool, msg.value)
            except Exception as e:
                logger.info("Error while processing message: ", e)
                await asyncio.sleep(1)

    finally:
        await consumer.stop()

