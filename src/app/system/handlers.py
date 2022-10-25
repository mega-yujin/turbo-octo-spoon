from http import HTTPStatus

from fastapi.responses import JSONResponse


def check_status():
    status: int = HTTPStatus.OK.value
    content = {"result": 'ok', "detail": "service ready"}
    return JSONResponse(status_code=status, content=content)
