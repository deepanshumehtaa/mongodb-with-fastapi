from fastapi import APIRouter, Depends, Body, Response, Request
from src.resources.base import BaseResponse
from src.resources import auth


auth_router = APIRouter()


@auth_router.post("/auth/signup", tags=["auth"])
async def reg(
        username: str = Body(..., embed=True),
        password: str = Body(..., embed=True, max_length=20, min_length=3),
) -> Response:
    return await auth.sign_up(username, password)


@auth_router.post("/auth/login", tags=["auth"])
async def login(
        username: str = Body(..., embed=True),
        password: str = Body(..., embed=True),
) -> Response:
    return await auth.login(username, password)


@auth_router.post(
    "/auth/change_password",
    tags=["auth"],
    dependencies=[Depends(auth.login_required)],
)
async def change_password(
        request: Request,
        password: str = Body(..., embed=True),
        old_password: str = Body(..., embed=True),
) -> Response:
    return await auth.change_password(request.state.user.username, password, old_password)


@auth_router.post(
    "/auth/logout",
    tags=["auth"],
    dependencies=[Depends(auth.login_required)],
)
async def logout(request: Request) -> Response:
    return await auth.logout(request.state.user)


@auth_router.get(
    "/auth/info",
    tags=["auth"],
    dependencies=[Depends(auth.login_required)],
)
async def info(request: Request) -> BaseResponse:
    return BaseResponse(data=request.state.user.dict())
