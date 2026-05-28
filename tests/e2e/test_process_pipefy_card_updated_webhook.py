from datetime import datetime

from src.domain.enums.client_enum import ClientPriority, ClientStatus
from src.infra.models.client_model import ClientModel


def test_should_process_webhook_success(client, db_session, faker):
    email = faker.email()

    client.post(
        "/clientes/",
        json={
            "cliente_nome": faker.name(),
            "cliente_email": email,
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 300000,
        },
    )

    payload = {
        "event_id": "evt_1",
        "card_id": "card_1",
        "cliente_email": email,
        "timestamp": datetime.utcnow().isoformat(),
    }

    response = client.post("/webhooks/pipefy/card-updated", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_should_not_process_duplicate_event(client, db_session, faker):
    email = faker.email()

    client.post(
        "/clientes/",
        json={
            "cliente_nome": faker.name(),
            "cliente_email": email,
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 300000,
        },
    )

    payload = {
        "event_id": "evt_duplicate",
        "card_id": "card_1",
        "cliente_email": email,
        "timestamp": datetime.utcnow().isoformat(),
    }

    response1 = client.post("/webhooks/pipefy/card-updated", json=payload)
    response2 = client.post("/webhooks/pipefy/card-updated", json=payload)

    assert response1.status_code == 200
    assert response1.json()["status"] == "success"

    assert response2.status_code == 200
    assert response2.json()["status"] == "already_processed"


def test_should_return_client_not_found(client):
    payload = {
        "event_id": "evt_404",
        "card_id": "card_404",
        "cliente_email": "notfound@test.com",
        "timestamp": datetime.utcnow().isoformat(),
    }

    response = client.post("/webhooks/pipefy/card-updated", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "client_not_found"


def test_should_set_high_priority(client, db_session, faker):
    email = faker.email()

    client.post(
        "/clientes/",
        json={
            "cliente_nome": faker.name(),
            "cliente_email": email,
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 300000,
        },
    )

    payload = {
        "event_id": "evt_high",
        "card_id": "card_1",
        "cliente_email": email,
        "timestamp": datetime.utcnow().isoformat(),
    }

    client.post("/webhooks/pipefy/card-updated", json=payload)

    db_client = db_session.query(ClientModel).filter_by(cliente_email=email).first()

    assert db_client.prioridade == ClientPriority.HIGH
    assert db_client.status == ClientStatus.PROCESSED


def test_should_set_normal_priority(client, db_session, faker):
    email = faker.email()

    client.post(
        "/clientes/",
        json={
            "cliente_nome": faker.name(),
            "cliente_email": email,
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 100000,
        },
    )

    payload = {
        "event_id": "evt_normal",
        "card_id": "card_1",
        "cliente_email": email,
        "timestamp": datetime.utcnow().isoformat(),
    }

    client.post("/webhooks/pipefy/card-updated", json=payload)

    db_client = db_session.query(ClientModel).filter_by(cliente_email=email).first()

    assert db_client.prioridade == ClientPriority.NORMAL
    assert db_client.status == ClientStatus.PROCESSED
