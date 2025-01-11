import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Replace with your own PostgreSQL instance
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
print("YYY_ ", DB_USER, DB_PASSWORD)
DB_HOST= os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


print("XXX_ ", DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)    