from aiokafka import AIOKafkaProducer
from core.config import settings
import json
import logging
import asyncio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

producer: AIOKafkaProducer | None = None

async def init_kafka_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            )
    try:
        await asyncio.wait_for(producer.start(), timeout=10)
        logger.info("Kafka producer started")
        logger.info(producer)
    except asyncio.TimeoutError:
        logger.error("Timeout connection to kafka")
    except Exception as e:
        logger.error(f"Failed to start Kafka producer: {e}")

async def close_kafka_producer():
    global producer
    if producer:
        await producer.stop()
        logger.info("Kafka producer stopped")

def get_producer():
    global producer
    return producer
