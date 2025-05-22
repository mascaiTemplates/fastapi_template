from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
import asyncio
from alembic.config import Config
from alembic import command

from models.users import User
from schemas.users import UserSchema, BaseUserSchema
from database.session import get_db
from api.v1.users import users_router

application = FastAPI()
application.include_router(users_router)

@application.on_event("startup")
async def startup_event():
    # Run alembic migrations
    alembic_cfg = Config("alembic.ini")
    try:
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(f"Error running migrations: {e}")
        raise e

@application.get("/health_check")
async def health_check():
    return {"Hello": "World"}


