from sqlalchemy.orm import Session
from app.db.schema import User
from typing import List

class UserService:
    def __init__(self, session: Session):
        self._db = session

    def create_user(self, name: str) -> User:
        user = User(name=name)
        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)
        return user
    
    def list_users(self) -> List[User]:
        return self._db.query(User).all()
    