from fastapi import APIRouter

from app.api.v1.endpoints import notes
from app.api.v1.endpoints import auth


api_router = APIRouter()
api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])