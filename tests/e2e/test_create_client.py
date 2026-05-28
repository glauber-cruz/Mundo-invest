from src.infra.models.client_model import ClientModel


def test_should_create_client(api, db_session, faker):
    email = faker.email()

    payload = {
        "cliente_nome": faker.name(),
        "cliente_email": email,
        "tipo_solicitacao": "Atualização cadastral",
        "valor_patrimonio": 250000,
    }

    response = api.post("/clientes/", json=payload)

    assert response.status_code == 201
    assert response.json()["message"] == "Client created successfully"

    db_client = db_session.query(ClientModel).filter_by(cliente_email=email).first()

    assert db_client is not None
    assert db_client.cliente_nome == payload["cliente_nome"]
    assert db_client.valor_patrimonio == payload["valor_patrimonio"]
    assert db_client.status == "Aguardando Análise"


def test_should_fail_with_invalid_email(api, faker):
    payload = {
        "cliente_nome": faker.name(),
        "cliente_email": "invalid-email",
        "tipo_solicitacao": "Atualização cadastral",
        "valor_patrimonio": 100000,
    }

    response = api.post("/clientes/", json=payload)

    assert response.status_code == 422


def test_should_not_allow_duplicate_email(api, db_session, faker):
    email = faker.email()

    payload = {
        "cliente_nome": faker.name(),
        "cliente_email": email,
        "tipo_solicitacao": "Atualização cadastral",
        "valor_patrimonio": 250000,
    }

    api.post("/clientes/", json=payload)
    response = api.post("/clientes/", json=payload)

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already exists"
