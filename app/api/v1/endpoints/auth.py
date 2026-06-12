# app/api/v1/endpoints/auth.py
from typing_extensions import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError
from pydantic import BaseModel
from typing_extensions import Annotated
from app.core.jwt import create_access_token, create_refresh_token, decode_token
from app.schemas.user import UserCreate, UserRead
from app.schemas.token import Token
from app.services.user_service import UserService, UserAlreadyExistsError
from app.api.v1.dependencies import get_user_service

router = APIRouter()


# Could live in token.py alongside Token — inline here for one field.
class RefreshRequest(BaseModel):
    refresh_token: str


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def register(
    user_in: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserRead:
    try:
        return service.register(user_in)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )


@router.post("/login", response_model=Token)
def login(
    service: Annotated[UserService, Depends(get_user_service)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = service.authenticate(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(
        access_token=create_access_token(user.id),
        refresh_token=create_refresh_token(user.id),
    )


@router.post("/refresh", response_model=Token)
def refresh(
    body: RefreshRequest,
) -> Token:
    try:
        claims = decode_token(body.refresh_token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    if claims.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    return Token(access_token=create_access_token(claims["sub"]))