from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.application.dtos.create_client_dto import CreateClientDTO
from src.application.use_cases.create_client import CreateClientUseCase
from src.infra.database.database import get_db
from src.infra.gateways.pipefy.pipefy_gateway import PipefyGateway
from src.infra.repositories.client_repo import ClientRepository
from src.presentation.schemas.clients_schema import CreateClientSchema

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.post("/", status_code=201)
def create_client(payload: CreateClientSchema, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    pipefy_gateway = PipefyGateway()

    use_case = CreateClientUseCase(
        client_repository=client_repository, pipefy_gateway=pipefy_gateway
    )

    payload_dto = CreateClientDTO(
        cliente_nome=payload.cliente_nome,
        cliente_email=payload.cliente_email,
        tipo_solicitacao=payload.tipo_solicitacao,
        valor_patrimonio=payload.valor_patrimonio,
    )

    use_case.execute(payload_dto)
    return {"message": "Client created successfully"}
