import aiomysql
from core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init_db_pool():
    pool = await aiomysql.create_pool(**settings.DB_CONFIG)
    logger.info("MySql pool ready")
    return pool

async def close_db_pool(pool):
    pool.close()
    await pool.wait_closed()

