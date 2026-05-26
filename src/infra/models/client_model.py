import uuid

from sqlalchemy import Numeric, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database.database import Base
from datetime import datetime

from src.domain.enums.client_enum import ClientStatus

class ClientModel(Base):
    __tablename__ = "clients"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    cliente_nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cliente_email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )

    tipo_solicitacao: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    valor_patrimonio: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default=ClientStatus.WAITING_ANALYSIS.value
    )

    prioridade: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
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