from src.schemas import CustomBase

from pydantic import PositiveInt, Field, EmailStr


class UserResponse(CustomBase):
    id: PositiveInt
    username: str = Field(..., min_length=5, max_length=30)
    email: EmailStr
    is_admin: bool 