from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str = "User1"
    email: str = "user1@gmail.com"
    is_active: bool = True

class User(UserBase):
    id: int

class UserCreate(UserBase):
    pass

class UserPatch(BaseModel):
    name: Optional[str] = "DefaultName"
    email: Optional[str] = "DefaultEmail"
    is_active: Optional[bool] = None
