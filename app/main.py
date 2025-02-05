from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from models.users import User
from schemas.users import UserSchema, BaseUserSchema
from database.session import get_db
from api.v1.users import users_router

application = FastAPI()
application.include_router(users_router)

@application.get("/health_check")
def health_check():
    return {"Hello": "World"}


