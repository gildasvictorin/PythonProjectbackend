from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from src.users.models import User
from src.users.schemas import UserResponse, UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

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
@router.post("/", response_model=UserResponse)
async def create_user(payload: UserCreate, session: AsyncSession = Depends(get_async_session)):
    new_user = User(
        username=payload.username,
        password=payload.password,
        email=payload.email,
        is_admin=payload.is_admin
    )
    session.add(new_user)
    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already in user")
    return new_user

#How to get, modify and delete USER
@router.get("/{user_id}", response_model=UserResponse)
async def get_users(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.id == user_id)
    query_result = await session.scalars(query)
    result = query_result.first()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

#modify user and go to schemas.py
##to modify user keeping all models created adding new class

@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, payload: UserUpdate, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.id == user_id)
    query_result = await session.scalars(query)
    result = query_result.first()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in payload.model_dump().items():
        if value is not None:
            setattr(result, field, value)

    try:
        await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already in user")
    return result



