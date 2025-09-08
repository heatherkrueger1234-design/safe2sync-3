# 🚀 FastAPI Authentication Backend

A simple backend boilerplate built with **FastAPI**, **JWT Authentication**, and **SQLAlchemy** (with SQLite/Postgres support).  
This project is structured to be clean, scalable, and production-ready.

---

## 📂 Project Structure

```
backend/
├── .env                # Environment variables (never commit this)
├── .gitignore          # Ignore files for git
├── requirements.txt    # Python dependencies
└── app/
    ├── __init__.py
    ├── main.py         # FastAPI entrypoint
    ├── auth.py         # JWT authentication manager
    ├── models.py       # Pydantic & DB models
    ├── database.py     # SQLAlchemy DB connection
    └── routes/
        ├── __init__.py
        ├── auth_routes.py
        └── users.py
```

---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO/backend
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.\.venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Create a `.env` file inside `backend/`:
```env
SECRET_KEY=change_this_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
DATABASE_URL=sqlite:///./test.db
```

👉 SECRET_KEY জেনারেট করার জন্য:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Run the server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Now visit: [http://localhost:8000/docs](http://localhost:8000/docs) 🎉

---

## 🔑 Authentication Flow

1. **Login to get a token**  
   - Endpoint: `POST /auth/token`  
   - Request body:
     ```json
     {
       "username": "alice",
       "password": "secret123"
     }
     ```
   - Response:
     ```json
     {
       "access_token": "your.jwt.token.here",
       "token_type": "bearer"
     }
     ```

2. **Access protected route**  
   - Endpoint: `GET /users/me`  
   - Headers:
     ```
     Authorization: Bearer your.jwt.token.here
     ```
   - Response:
     ```json
     {
       "username": "alice"
     }
     ```

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – API framework  
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM  
- [Passlib](https://passlib.readthedocs.io/) – Password hashing  
- [Python-JOSE](https://python-jose.readthedocs.io/) – JWT handling  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

---

## 📌 Todo (Next Steps)

- ✅ JWT Authentication  
- ✅ Basic User model  
- ⬜ Database migrations (Alembic)  
- ⬜ Refresh tokens  
- ⬜ Docker support  
- ⬜ GitHub Actions CI/CD  

---

## 📜 License

This project is open-source and available under the **MIT License**.
