from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from alembic.config import Config
from database.session import engine

from models.users import User
from schemas.users import UserSchema, BaseUserSchema
from database.session import get_db
from api.v1.users import users_router

application = FastAPI()
application.include_router(users_router)


@application.get("/health_check")
async def health_check():
    return {"Hello": "World"}


