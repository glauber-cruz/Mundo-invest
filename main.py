from fastapi import FastAPI

from src.presentation.routes.clients import router as clients_router
from src.presentation.routes.webhooks import router as webhooks_router

from src.infra.database.database import Base
from src.infra.database.database import engine

app = FastAPI()

app.include_router(clients_router)
app.include_router(webhooks_router)

Base.metadata.create_all(bind=engine)