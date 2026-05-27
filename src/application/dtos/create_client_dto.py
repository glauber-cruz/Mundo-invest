from dataclasses import dataclass

from pydantic import EmailStr


@dataclass(frozen=True)
class CreateClientDTO:
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float
