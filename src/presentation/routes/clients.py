from fastapi import APIRouter
from src.presentation.schemas.clients_schema import CreateClientSchema

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

@router.post("/")
def create_client(payload: CreateClientSchema):
    return {"message": "Client created"}