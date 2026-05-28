from src.application.dtos.pipefy_card_update_webhook_dto import (
    PipefyCardUpdateWebhookDTO,
)
from src.domain.enums.client_enum import ClientPriority, ClientStatus
from src.infra.database.uow import UnitOfWork
from src.infra.mappers.client import to_domain, to_model
from src.infra.gateways.pipefy.pipefy_gateway import PipefyGateway
from src.infra.models.processed_events_model import ProcessedEventModel


class ProcessPipefyCardUpdatedWebhookUseCase:
    def __init__(self, uow: UnitOfWork, pipefy_gateway: PipefyGateway):
        self.uow = uow
        self.pipefy_gateway = pipefy_gateway

    def execute(self, payload: PipefyCardUpdateWebhookDTO):
        priority_value = 200_000

        with self.uow:
            event_already_processed = self.uow.processed_events.event_already_processed(
                payload.event_id
            )

            if event_already_processed:
                return {"status": "already_processed"}

            client_data = self.uow.clients.get_by_email(payload.cliente_email)

            if not client_data:
                return {"status": "client_not_found"}

            client = to_domain(client_data)
            client.process()

            processed_event = ProcessedEventModel(
                event_id=payload.event_id,
                card_id=payload.card_id,
                processed_at=payload.timestamp,
            )

            self.uow.processed_events.create(processed_event)
            self.uow.clients.update(to_model(client))

        self.pipefy_gateway.update_card_fields(
            card_id=payload.card_id,
            status=client.status,
            prioridade=client.prioridade,
        )

        return {"status": "success"}
