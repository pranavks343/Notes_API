from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate


class NoteRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, note_in: NoteCreate) -> Note:
        note = Note(**note_in.model_dump())
        self._session.add(note)
        self._session.commit()
        self._session.refresh(note)
        return note

    def get_by_id(self, note_id: int) -> Note | None:
        return self._session.get(Note, note_id)

    def list_all(self) -> list[Note]:
        return self._session.scalars(select(Note)).all()

    def delete(self, note_id: int) -> bool:
        note = self._session.get(Note, note_id)
        if note is None:
            return False
        self._session.delete(note)
        self._session.commit()
        return True