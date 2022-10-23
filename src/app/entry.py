from fastapi import FastAPI
from app.api.routes import setup_routes
from app.system.middlewares import setup_middlewares
import uvicorn


def prepare_app():
    app = FastAPI()
    setup_routes(app)
    # setup_middlewares(app)
    return app


def start_app():
    uvicorn.run(
        app=prepare_app(),
        host='127.0.0.1',
        port=8000,
    )


if __name__ == "__main__":
    start_app()
