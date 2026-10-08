from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import User
from app.database.postgres import get_db
from app.models.user_model import User as UserModel

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)
# GET - Fetch users from PostgreSQL
@router.get("")
def get_users(db: Session = Depends(get_db)):

    users = db.query(UserModel).all()
    data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        }
        for user in users
    ]
    return {
        "status": 200,
        "message": "Users retrieved successfully",
        "data": data
    }

# POST - Save user to PostgreSQL
@router.post("", status_code=201)
def create_user(
    user: User,
    db: Session = Depends(get_db)
):

    new_user = UserModel(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "status": 201,
        "message": "User created successfully",
        "data": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "age": new_user.age
        }
    }