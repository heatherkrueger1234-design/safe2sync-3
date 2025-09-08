# 🚀 FastAPI Authentication Backend

A simple backend boilerplate built with **FastAPI**, **JWT Authentication**, and **SQLAlchemy** (with SQLite/Postgres support).  
This project is structured to be clean, scalable, and production-ready.

---

## 📂 Project Structure

backend/
├── .env # Environment variables (never commit this)
├── .gitignore # Ignore files for git
├── requirements.txt # Python dependencies
└── app/
├── init.py
├── main.py # FastAPI entrypoint
├── auth.py # JWT authentication manager
├── models.py # Pydantic & DB models
├── database.py # SQLAlchemy DB connection
└── routes/
├── init.py
├── auth_routes.py
└── users.py



---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo/backend


2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.\.venv\Scripts\activate    # Windows

3. Install dependencies
pip install -r requirements.txt


