from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.note_repository import NoteRepository
from app.services.note_service import NoteService


def get_note_repository(
    db: Annotated[Session, Depends(get_db)],
) -> NoteRepository:
    return NoteRepository(db)


def get_note_service(
    repo: Annotated[NoteRepository, Depends(get_note_repository)],
) -> NoteService:
    return NoteService(repo)