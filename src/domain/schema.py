from pydantic import BaseModel
from uuid import uuid4
from typing import Optional
from datetime import datetime

class Model_Create(BaseModel):
    unique_id: str = (uuid4())
    name: str
    age: int
    gender: str
    status: bool = True
    created_at: Optional[str] = datetime.now()

class Model_Up(BaseModel):
    name: str
    age: int
    gender: str
    created_at: Optional[str] = datetime.now()

class Soft(BaseModel):
    status: bool

