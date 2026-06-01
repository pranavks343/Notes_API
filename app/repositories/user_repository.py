from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.users import User 


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, email: str, hashed_password: str) -> User:
        user = User(email=email, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.session.scalars(stmt).first()

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)