from fastapi import APIRouter
from src.presentation.schemas.webhooks_schema import PipefyCardUpdatedSchema

router = APIRouter(
    prefix="/webhooks",
    tags=["webhooks"]
)

@router.post("/pipefy/card-updated")
def pipefy_card_updated(payload: PipefyCardUpdatedSchema):
    return {"message": "Pipefy card updated"}