from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.dependencies import get_note_service
from app.schemas.note import NoteCreate, NoteRead
from app.services.note_service import NoteService, NoteValidationError

router = APIRouter()


@router.post("/", status_code=201, response_model=NoteRead)
def create_note(
    note_in: NoteCreate,
    service: Annotated[NoteService, Depends(get_note_service)],
):
    try:
        return service.create_note(note_in)
    except NoteValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/", status_code=200, response_model=list[NoteRead])
def list_notes(
    service: Annotated[NoteService, Depends(get_note_service)],
):
    return service.list_notes()


@router.get("/{note_id}", status_code=200, response_model=NoteRead)
def get_note(
    note_id: int,
    service: Annotated[NoteService, Depends(get_note_service)],
):
    note = service.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: int,
    service: Annotated[NoteService, Depends(get_note_service)],
):
    if not service.delete_note(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
    return None