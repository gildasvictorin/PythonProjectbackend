from typing import Optional
from src.schemas import CustomBase
from datetime import datetime
from pydantic import PositiveInt, Field, EmailStr


class UserResponse(CustomBase):
    id: PositiveInt
    username: str = Field(..., min_length=5, max_length=50, examples=["ciccio"])
    email: EmailStr
    is_admin: bool
    created_id: datetime


#how to create user and create it inside router with decorator

class UserCreate(CustomBase):
    username: str = Field(..., min_length=5, max_length=50, examples=["ciccio"])
    email: EmailStr
    password: str = Field(..., min_length=5, max_length=30, examples=["ciccio123"])
    is_admin: bool = Field(False)

#to modify user keeping all models create and import optional
class UserUpdate(CustomBase):
    username: Optional[str] = Field(None, min_length=5, max_length=50, examples=["ciccio"])
    email: Optional[EmailStr] = Field(None)
    password: Optional[str] = Field(None, min_length=5, max_length=30, examples=["ciccio123"])
    is_admin: Optional[bool] = Field(None)
