from src.domain.entities.client_entity import Client
from src.domain.enums.client_enum import ClientStatus, ClientPriority
from src.infra.models.client_model import ClientModel

def to_domain(model: ClientModel) -> Client:
    return Client(
        id=model.id,
        cliente_nome=model.cliente_nome,
        cliente_email=model.cliente_email,
        tipo_solicitacao=model.tipo_solicitacao,
        valor_patrimonio=float(model.valor_patrimonio),
        status=ClientStatus(model.status),
        prioridade=ClientPriority(model.prioridade) if model.prioridade else None,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )

def to_model(domain: Client) -> ClientModel:
    return ClientModel(
        id=domain.id,
        cliente_nome=domain.cliente_nome,
        cliente_email=domain.cliente_email,
        tipo_solicitacao=domain.tipo_solicitacao,
        valor_patrimonio=domain.valor_patrimonio,
        status=domain.status.value,
        prioridade=domain.prioridade.value if domain.prioridade else None,
        created_at=domain.created_at,
        updated_at=domain.updated_at,
    )