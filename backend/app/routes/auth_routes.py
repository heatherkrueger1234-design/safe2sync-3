# backend/app/routes/auth_routes.py
from fastapi import APIRouter, HTTPException
from app.models import Token, UserIn
from app.auth import auth_manager, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()

# VERY simple in-memory "user DB" for demo.
fake_users_db = {
    "alice": {
        "username": "alice",
        "full_name": "Alice Example",
        "email": "alice@example.com",
        "hashed_password": auth_manager.get_password_hash("secret123"),
        "disabled": False,
    }
}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: UserIn):
    user = fake_users_db.get(form_data.username)
    if not user or not auth_manager.verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_manager.create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

