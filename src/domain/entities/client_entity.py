from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.client_enum import ClientPriority, ClientStatus


@dataclass
class Client:
    id: str
    cliente_nome: str
    cliente_email: str
    tipo_solicitacao: str
    valor_patrimonio: float
    status: ClientStatus
    prioridade: ClientPriority | None
    created_at: datetime
    updated_at: datetime

    def is_high_priority(self) -> bool:
        return self.valor_patrimonio >= 200_000

    def process(self):
        self.status = ClientStatus.PROCESSED
        self.prioridade = (
            ClientPriority.HIGH if self.is_high_priority() else ClientPriority.NORMAL
        )
