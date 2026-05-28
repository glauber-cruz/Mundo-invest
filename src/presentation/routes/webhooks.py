from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.application.dtos.pipefy_card_update_webhook_dto import (
    PipefyCardUpdateWebhookDTO,
)
from src.application.use_cases.process_pipefy_card_updated_webhook import (
    ProcessPipefyCardUpdatedWebhookUseCase,
)
from src.infra.database.database import get_db
from src.infra.database.uow import UnitOfWork
from src.infra.gateways.pipefy.pipefy_gateway import PipefyGateway
from src.presentation.schemas.webhooks_schema import PipefyCardUpdatedSchema

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/pipefy/card-updated")
def pipefy_card_updated(
    payload: PipefyCardUpdatedSchema, db: Session = Depends(get_db)
):
    uow = UnitOfWork(db)
    pipefy_gateway = PipefyGateway()

    payload_dto = PipefyCardUpdateWebhookDTO(
        event_id=payload.event_id,
        card_id=payload.card_id,
        cliente_email=payload.cliente_email,
        timestamp=payload.timestamp,
    )

    use_case = ProcessPipefyCardUpdatedWebhookUseCase(uow=uow, pipefy_gateway=pipefy_gateway)
    response = use_case.execute(payload_dto)

    return response