# backend/app/routes/users.py
from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter()

@router.get("/me")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
