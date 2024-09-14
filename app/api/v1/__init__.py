from fastapi import APIRouter
from .routers.posts import router as posts_router
from core.config import settings

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(
    router=posts_router,
    prefix=settings.api.v1.posts_prefix,
)
