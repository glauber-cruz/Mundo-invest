from src.application.dtos.pipefy_card_update_webhook_dto import (
    PipefyCardUpdateWebhookDTO,
)

from src.infra.repositories.processed_events_repo import ProcessedEventsRepository
from src.infra.repositories.client_repo import ClientRepository

from fastapi import HTTPException
from src.domain.enums.client_enum import ClientPriority

from src.domain.enums.client_enum import ClientStatus
from src.infra.models.processed_events_model import ProcessedEventModel
from src.infra.database.uow import UnitOfWork


class ProcessPipefyCardUpdatedWebhookUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def execute(self, payload: PipefyCardUpdateWebhookDTO):
        priority_value = 200_200

        with self.uow:
            event_already_processed = self.uow.processed_events.event_already_processed(
                payload.event_id
            )

            if event_already_processed:
                return {"status": "already_processed"}

            client = self.uow.clients.get_by_email(payload.cliente_email)

            if not client:
                return {"status": "client_not_found"}

            client.prioridade = (
                ClientPriority.HIGH
                if client.valor_patrimonio >= priority_value
                else ClientPriority.NORMAL
            )

            client.status = ClientStatus.PROCESSED

            processed_event = ProcessedEventModel(
                event_id=payload.event_id,
                card_id=payload.card_id,
                processed_at=payload.timestamp,
            )

            self.uow.processed_events.create(processed_event)
            self.uow.clients.update(client)

        return {"status": "success"}
