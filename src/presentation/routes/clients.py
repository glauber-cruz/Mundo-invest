from fastapi import APIRouter

router = APIRouter()

@router.post("/clients")
def create_client():
    return {"message": "Client created"}