import traceback
from typing import Callable, Union, List
from fastapi.exceptions import RequestValidationError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import StreamingResponse, JSONResponse


class APIError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class AuthError(APIError):
    pass


async def request_validation_exception_handler(_: Request,
                                               exc: RequestValidationError) -> JSONResponse:
    x = exc.errors()
    return JSONResponse({
        "err_code": 402,
        "msg": "Incorrect request parameters",
        "data": x
    })


class ErrorCatcherMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request,
                             call_next: Callable) -> Union[StreamingResponse, JSONResponse]:
        try:
            response: StreamingResponse = await call_next(request)
            if response.status_code > 499:
                chunks: List[bytes] = []
                async for chunk in response.body_iterator:
                    if not isinstance(chunk, bytes):
                        chunk = chunk.encode("utf-8")
                        chunks.append(chunk)
                raw_body = b"".join(chunks)
                raise APIError(f"Http Error！\nstatus code: {response.status_code}\n{raw_body}")

        except AuthError as e:
            return JSONResponse({"err_code": 401, "msg": e.msg})

        except APIError as e:
            return JSONResponse({"err_code": 400, "msg": e.msg})

        except Exception as e:
            return JSONResponse({
                "err_code": 500,
                "msg": f"System internal error！\ne: {e}\n{traceback.format_exc()}"
            })
        return response
