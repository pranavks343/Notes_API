from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models.

    DeclarativeBase in FastAPI + SQLAlchemy is used to create a common base class so all ORM models can inherit database mapping behavior (tables, columns, relationships, metadata) automatically.
    """
    pass