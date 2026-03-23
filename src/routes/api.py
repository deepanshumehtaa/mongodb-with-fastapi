from fastapi import APIRouter
from src.routes.bill import bill_router
from src.routes.category import cat_router
from src.routes.book import book_router
from src.routes.hitokoto import hitokoto_router


router = APIRouter()

router.include_router(bill_router)
router.include_router(cat_router)
router.include_router(book_router)
router.include_router(hitokoto_router)
