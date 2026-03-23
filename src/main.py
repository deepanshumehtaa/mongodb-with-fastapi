"""
uvicorn main:app --port=8001 --reload

uvicorn main:app --port=8001 --reload --workers 4
"""

import logging

from fastapi import FastAPI, Query
from starlette.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from src.framework.asynchronous import AsyncExecutor
from src.framework.errors import ErrorCatcherMiddleware, request_validation_exception_handler

from src.routes.auth import auth_router
from src.routes.api import router as api_router
from src.frontend.api import router as frontend_router

logger = logging.getLogger(__name__)

application = FastAPI(
    title="My Fav FastAPI project",
    version="1.0.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # not render `schema` page in bottom of swagger
        "tryItOutEnabled": True,
        "docExpansion": "none",  # collapse all
    }
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
application.add_exception_handler(RequestValidationError, request_validation_exception_handler)
application.add_middleware(ErrorCatcherMiddleware)

@application.get("/health")
async def health(trace_id = Query(default="")):
    logger.info("health api called !")
    return {
        "success": True
    }

application.include_router(auth_router)
application.include_router(api_router, prefix="/madbook/api")

# No Need
# application.include_router(frontend_router, prefix="/madbook")

# application.mount(
#     "/madbook/static",
#     StaticFiles(directory="frontend/static"),
#     name="static",
# )

application.state.AE = AsyncExecutor()
# application.add_event_handler("startup", application.state.AE.startup)
# application.add_event_handler("shutdown", application.state.AE.shutdown)

