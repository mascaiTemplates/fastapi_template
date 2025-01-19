from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from models.users import User
from schemas.users import UserSchema, BaseUserSchema
from database.session import get_db

users_router = APIRouter()


@users_router.get("/users", tags=["user"])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@users_router.post("/users", response_model=UserSchema, tags=["user"])
def create_user(user_data: BaseUserSchema, db: Session = Depends(get_db)):
    query = db.query(User).filter(User.name == user_data.name).first()
    if query:
        raise HTTPException(status_code=400, detail="User already exist")
    new_user = User(name=user_data.name, age=user_data.age)
    db.add(new_user)
    db.commit()
    return new_user