from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict, Any

from models.users import User
from schemas.users import UserSchema, BaseUserSchema
from database.session import get_db

users_router = APIRouter()


@users_router.get("/users", tags=["user"])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()


@users_router.post("/users", response_model=UserSchema, tags=["user"])
async def create_user(user_data: BaseUserSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.name == user_data.name))
    query = result.scalar_one_or_none()
    if query:
        raise HTTPException(status_code=400, detail="User already exist")
    new_user = User(name=user_data.name, age=user_data.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user