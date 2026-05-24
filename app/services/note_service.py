from app.repositories.note_repository import NoteRepository
from app.schemas.note import NoteCreate, NoteInDB


class NoteValidationError(Exception):
    """Raised when note data violates business rules (e.g., spam)."""
    pass


class NoteService:

    def __init__(self,repository:NoteRepository):
        self._repo=repository

    def create_note(self,note_in:NoteCreate)->NoteInDB:
        if "spam" in note_in.title.lower():
            raise NoteValidationError("Note content cannot contain 'spam'.")
        return self._repo.create(note_in)
    
    def get_note(self,note_id:int)->NoteInDB|None:
        return self._repo.get_by_id(note_id)
    
    def list_notes(self)->list[NoteInDB]:
        return self._repo.list_all()
    
    def delete_note(self,note_id:int)->bool:
        return self._repo.delete(note_id)
        
    