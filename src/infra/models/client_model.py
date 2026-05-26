import uuid

from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.infra.database.database import Base

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
        nullable=False
    )

    prioridade: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )