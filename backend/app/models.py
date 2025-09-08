# backend/app/models.py
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

