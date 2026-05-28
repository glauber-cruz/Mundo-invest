from fastapi import HTTPException

from src.application.dtos.create_client_dto import CreateClientDTO
from src.domain.enums.client_enum import ClientStatus
from src.infra.gateways.pipefy.pipefy_gateway import PipefyGateway
from src.infra.models.client_model import ClientModel
from src.infra.repositories.client_repo import ClientRepository


class CreateClientUseCase:
    def __init__(
        self, client_repository: ClientRepository, pipefy_gateway: PipefyGateway
    ):
        self.client_repository = client_repository
        self.pipefy_gateway = pipefy_gateway

    def execute(self, payload: CreateClientDTO):
        email_already_exists = self.client_repository.email_already_exists(
            payload.cliente_email
        )

        if email_already_exists:
            raise HTTPException(status_code=409, detail="Email already exists")

        client_model = ClientModel(
            cliente_nome=payload.cliente_nome,
            cliente_email=payload.cliente_email,
            tipo_solicitacao=payload.tipo_solicitacao,
            valor_patrimonio=payload.valor_patrimonio,
            status=ClientStatus.WAITING_ANALYSIS,
        )

        self.client_repository.create(client_model)

        self.pipefy_gateway.create_card(
            cliente_nome=payload.cliente_nome,
            cliente_email=payload.cliente_email,
            valor_patrimonio=payload.valor_patrimonio,
            tipo_solicitacao=payload.tipo_solicitacao,
            status=ClientStatus.WAITING_ANALYSIS,
        )
