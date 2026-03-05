from fastapi import APIRouter

from app.api.v1.routes import convert


api_router = APIRouter()

api_router.include_router(convert.router, prefix="/convert", tags=["conversion"])

