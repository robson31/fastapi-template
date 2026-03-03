from fastapi import APIRouter, Depends
from app.models.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.db.session import SessionLocal
from app.db.session import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(session=db)


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user.name)


@router.get("/", response_model=list[UserRead])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()