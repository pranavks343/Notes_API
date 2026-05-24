from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import engine
"""
# from app.models.note import Note  
# from app.models.base import Base



# Base.metadata.create_all(bind=engine)

deleted for alembic, which is now used for database migrations. Alembic uses the models to generate migration scripts, so we need to import them in alembic/env.py instead.
"""

app = FastAPI(title=settings.app_name)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}



app.include_router(api_router, prefix=settings.api_v1_prefix)