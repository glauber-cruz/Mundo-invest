import uuid

from sqlalchemy import Numeric, DateTime
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infra.database.database import Base
from datetime import datetime

from src.domain.enums.client_enum import ClientStatus, ClientPriority
from sqlalchemy.types import Enum as SqlEnum

class ClientModel(Base):
    __tablename__ = "clients"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=uuid.uuid4
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

    status: Mapped[ClientStatus] = mapped_column(
        SqlEnum(ClientStatus),
        nullable=False,
        default=ClientStatus.WAITING_ANALYSIS
    )

    prioridade: Mapped[ClientPriority | None] = mapped_column(
        SqlEnum(ClientPriority),
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