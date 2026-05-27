from fastapi import APIRouter
from src.presentation.schemas.clients_schema import CreateClientSchema

from src.application.use_cases.create_client import CreateClientUseCase
from src.infra.repositories.client_repo import ClientRepository

from src.infra.database.database import get_db
from sqlalchemy.orm import Session

from fastapi import Depends
from src.application.dtos.create_client_dto import CreateClientDTO

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/", status_code=201)
def create_client(payload: CreateClientSchema, db: Session = Depends(get_db)):
    client_repository = ClientRepository(db)
    use_case = CreateClientUseCase(client_repository)

    payload_dto = CreateClientDTO(
        cliente_nome=payload.cliente_nome,
        cliente_email=payload.cliente_email,
        tipo_solicitacao=payload.tipo_solicitacao,
        valor_patrimonio=payload.valor_patrimonio,
    )

    use_case.execute(payload_dto)
    return {"message": "Client created successfully"}
