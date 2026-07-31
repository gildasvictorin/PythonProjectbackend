from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select
from src.users.models import User
from src.users.schemas import UserResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.databese import get_async_session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    query_result = await session.scalars(query)
    result = query_result.all()
    return result
#after this import in main.py(from src.users.routers import router as users_router)
# and app.include_router(users_router)