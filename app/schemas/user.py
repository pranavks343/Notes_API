from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)


class UserRead(BaseModel):

    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime


class UserInDB(UserRead):
    hashed_password: str 