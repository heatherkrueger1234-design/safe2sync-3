# backend/app/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
import os

# load .env so os.getenv in other modules can see values
load_dotenv()

app = FastAPI(title="My App")

# include routers
from app.routes import auth_routes, users
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"status": "ok"}
