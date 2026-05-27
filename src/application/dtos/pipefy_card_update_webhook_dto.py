from dataclasses import dataclass
from datetime import datetime

from pydantic import EmailStr


@dataclass(frozen=True)
class PipefyCardUpdateWebhookDTO:
    event_id: str
    card_id: str
    cliente_email: EmailStr
    timestamp: datetime
