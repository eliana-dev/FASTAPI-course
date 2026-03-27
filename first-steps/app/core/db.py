import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

DEFAULT_SQLITE_URL = f"sqlite:///{BASE_DIR / 'blog.db'}"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_SQLITE_URL)  ##motor://ruta


engine_kwargs = {}

if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {
        "check_same_thread": False
    }  ##permite que varios threads usen esta conexión

engine = create_engine(
    DATABASE_URL, echo=True, future=True, **engine_kwargs
)  

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=Session
)


class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()

