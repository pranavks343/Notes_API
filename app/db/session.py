from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.core.config import settings

# SQLite-specific: allow same connection across threads (FastAPI's threadpool uses many)
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

engine = create_engine(settings.database_url, connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def get_db()->Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()