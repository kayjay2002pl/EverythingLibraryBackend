from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.env_loader import SQLALCHEMY_DATABASE_URL

engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_size=25,
        max_overflow=10,
        pool_pre_ping=True,
    )

Base = declarative_base()
meta = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_session() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()