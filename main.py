from fastapi import FastAPI

from src.infra.config.enviroment import load_enviroment
from src.presentation.routes.clients import router as clients_router
from src.presentation.routes.webhooks import router as webhooks_router


def create_app() -> FastAPI:
    load_enviroment()
    app = FastAPI()

    app.include_router(clients_router)
    app.include_router(webhooks_router)

    return app


app = create_app()
