import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database.database import Base

from datetime import datetime

class ProcessedEventModel(Base):
    __tablename__ = "processed_events"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    event_id: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True
    )

    card_id: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    processed_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    created_at: Mapped[datetime] = mapped_column(
      DateTime,
      nullable=False,
      default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )