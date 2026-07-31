#from src.blog.routers import router as blog_router
from src.config import settings
from src.users.routers import router as users_router
from src.events.models import Event
from src.comments.models import Comment
from src.reservations.models import Reservation

from fastapi import FastAPI

app = FastAPI(
    title=settings.app_name
)

app.include_router(users_router)




