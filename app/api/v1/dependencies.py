from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.note_repository import NoteRepository
from app.services.note_service import NoteService
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


def get_note_repository(
    db: Annotated[Session, Depends(get_db)],
) -> NoteRepository:
    return NoteRepository(db)


def get_note_service(
    repo: Annotated[NoteRepository, Depends(get_note_repository)],
) -> NoteService:
    return NoteService(repo)


def get_user_repository(db: Annotated[Session, Depends(get_db)]) -> UserRepository:
    return UserRepository(db)

def get_user_service(
    repo: Annotated[UserRepository, Depends(get_user_repository)],
) -> UserService:
    return UserService(repo)