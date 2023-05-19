from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "sqlite:///./fastapi-practice.db"

engine = create_engine(sqlalchemy_database_url,
                       connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
