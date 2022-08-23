from fastapi import APIRouter

from api.api_v1 import authentication

api_router = APIRouter()
api_router.include_router(authentication.router, prefix="/authentication", tags=["authentication"])
