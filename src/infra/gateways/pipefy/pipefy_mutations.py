class PipefyMutations:
    # https://developers.pipefy.com/reference/create-a-card-with-the-required-fields-fulfilled#step-3-create-the-card-graphql-mutation
    CREATE_CARD = """
      mutation CreateCard(
          $pipe_id: ID!,
          $cliente_nome: String!,
          $cliente_email: String!,
          $valor_patrimonio: Float!,
          $tipo_solicitacao: String!,
          $status: String!
      ) {
        createCard(input: {
          pipe_id: $pipe_id,
          fields_attributes: [
            { field_id: "cliente_nome", field_value: $cliente_nome },
            { field_id: "cliente_email", field_value: $cliente_email },
            { field_id: "valor_patrimonio", field_value: $valor_patrimonio },
            { field_id: "tipo_solicitacao", field_value: $tipo_solicitacao },
            { field_id: "status", field_value: $status }
          ]
        }) {
          card {
            id
            title
          }
        }
      }
    """

    UPDATE_CARD_FIELDS = """
      mutation UpdateCardFields(
          $card_id: ID!,
          $status: String!,
          $prioridade: String!
      ) {
        updateCardFields(input: {
          card_id: $card_id,
          fields_attributes: [
            {
              field_id: "status",
              field_value: $status
            },
            {
              field_id: "prioridade",
              field_value: $prioridade
            }
          ]
        }) {
          card {
            id
            title
          }
        }
      }
    """
