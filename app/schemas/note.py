from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1, max_length=10000)
    tags: list[str] = Field(default_factory=list)##optional 


class NoteRead(BaseModel):  
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    tags: list[str]
    created_at: datetime


class NoteInDB(NoteRead):
    is_archived: bool = False