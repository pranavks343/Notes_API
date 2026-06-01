
from app.core.security import hash_password
from app.models.users import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserAlreadyExistsError(Exception):
    """Raised when attempting to register an email that already exists."""
    pass


class UserService:
    def __init__(self, repository: UserRepository):
        self._repo = repository

    def register(self, user_in: UserCreate) -> User:
        existing = self._repo.get_by_email(user_in.email)
        if existing is not None:
            raise UserAlreadyExistsError(
                f"User with email {user_in.email} already exists"
            )

        hashed = hash_password(user_in.password)
        return self._repo.create(email=user_in.email, hashed_password=hashed) 