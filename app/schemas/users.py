from typing import List, Dict, Any
from pydantic import BaseModel
from enum import Enum


class BaseUserSchema(BaseModel):
    name: str
    age: int


class UserSchema(BaseUserSchema):
    id: int