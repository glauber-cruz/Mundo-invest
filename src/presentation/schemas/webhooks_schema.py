from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from datetime import datetime


class PipefyCardUpdatedSchema(BaseModel):
    event_id: str = Field(max_length=100, description="ID do evento", example="evt_123")
    card_id: str = Field(
        max_length=100, description="ID do card do Pipefy", example="card_123"
    )
    cliente_email: EmailStr = Field(
        max_length=120, description="Email do cliente", example="cliente@gmail.com"
    )
    timestamp: datetime = Field(
        description="Timestamp do evento", example="2021-01-01T00:00:00Z"
    )
