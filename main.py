from fastapi import FastAPI

from src.presentation.routes.clients import router as clients_router
from src.presentation.routes.webhooks import router as webhooks_router

app = FastAPI()

app.include_router(clients_router)
app.include_router(webhooks_router)