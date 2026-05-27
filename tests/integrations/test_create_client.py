from src.infra.models.client_model import ClientModel


def test_should_create_client(client):
    response = client.post(
        "/clients/",
        json={
            "cliente_nome": "João Silva",
            "cliente_email": "joao@gmail.com",
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 250000
        }
    )

    assert response.status_code == 201

    body = response.json()

    assert body["message"] == "Client created successfully"