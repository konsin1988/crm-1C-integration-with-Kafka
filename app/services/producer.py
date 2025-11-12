from core.kafka import get_producer
from core.config import settings
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_to_kafka(message: dict):
    producer = get_producer()

    if not producer:
        raise RuntimeError("Kafka producer is not initialized")

    await producer.send_and_wait(
            settings.KAFKA_ACCOUNT_TOPIC,
            key=str(message['id']).encode('utf-8'),
            value=message
            )
    logger.info(f"Sent to Kafka: {message}")
