from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import settings


def _create_token(subject: str | int, expires_delta: timedelta, token_type: str) -> str:
    now=datetime.now(timezone.utc)

    claims={
        "sub": str(subject),
        "iat": now,
        "exp":now+expires_delta,
        "type":token_type,

    }

    return jwt.encode(claims, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def create_access_token(subject: str | int) -> str:
    return _create_token(
        subject,
        timedelta(minutes=settings.access_token_expire_minutes),
        "access",
    )


def create_refresh_token(subject: str | int) -> str:
    return _create_token(
        subject,
        timedelta(days=settings.refresh_token_expire_days),
        "refresh",
    )