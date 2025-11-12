from fastapi import APIRouter
from api.v1 import account, guid

api_router = APIRouter()
api_router.include_router(account.router, prefix="/account", tags=["accounts"])
api_router.include_router(guid.router, prefix="/guid", tags=["guid"])
