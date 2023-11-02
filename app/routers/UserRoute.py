from fastapi import APIRouter
from models.User import User

router = APIRouter()

@router.post("/user")
async def add_user(user: User):
    return {"username": user.userName}