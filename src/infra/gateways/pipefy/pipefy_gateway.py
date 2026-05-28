from src.infra.gateways.pipefy.pipefy_mutations import PipefyMutations
from os import getenv

class PipefyGateway:
  def __init__(self): pass

  def _send(self, mutation, variables): pass

  def create_card(self, cliente_nome, cliente_email, valor_patrimonio, tipo_solicitacao, status):
      mutation = PipefyMutations.CREATE_CARD

      variables = {
          "pipe_id": int(getenv("PIPE_ID")),
          "cliente_nome": cliente_nome,
          "cliente_email": cliente_email,
          "valor_patrimonio": valor_patrimonio,
          "tipo_solicitacao": tipo_solicitacao,
          "status": status,
      }

      return self._send(mutation, variables)


  def update_card_fields(self, card_id, status, prioridade):
    mutation = PipefyMutations.UPDATE_CARD_FIELDS

    variables = {
      "card_id": card_id,
      "status": status,
      "prioridade": prioridade,
    }

    return self._send(mutation, variables)