from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class CreateClientSchema(BaseModel):
    cliente_nome: str = Field(
      min_length=3,
      max_length=100,
      description="Nome do cliente",
      example="João da Silva"
    )
    cliente_email: EmailStr = Field(
      description="Email do cliente",
      example="cliente@gmail.com"
    )
    tipo_solicitacao: str = Field(
      description="Tipo de solicitação",
      example="Solicitação de crédito"
    )
    valor_patrimonio: float = Field(
      ge=0,
      max_digits=12,
      decimal_places=2,
      description="Valor do patrimônio do cliente",
      example=100000.00,
    )