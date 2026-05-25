from fastapi import APIRouter

router = APIRouter()

@router.post("/webhooks/pipefy/card-updated")
def pipefy_card_updated():
    return {"message": "Pipefy card updated"}