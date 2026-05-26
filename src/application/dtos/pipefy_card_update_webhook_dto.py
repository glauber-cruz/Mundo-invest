from dataclasses import dataclass
from pydantic import EmailStr
from datetime import datetime

@dataclass(frozen=True)
class PipefyCardUpdateWebhookDTO:
    event_id: str
    card_id: str
    cliente_email: EmailStr
    timestamp: datetime