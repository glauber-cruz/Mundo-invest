class PipefyMutations:
    CREATE_CARD = """
    mutation CreateCard(
        $pipe_id: ID!,
        $cliente_nome: String!,
        $cliente_email: String!,
        $valor_patrimonio: Float!,
        $tipo_solicitacao: String!
    ) {
      createCard(input: {
        pipe_id: $pipe_id,
        fields_attributes: [
          { field_id: "cliente_nome", field_value: $cliente_nome },
          { field_id: "cliente_email", field_value: $cliente_email },
          { field_id: "valor_patrimonio", field_value: $valor_patrimonio },
          { field_id: "tipo_solicitacao", field_value: $tipo_solicitacao }
        ]
      }) {
        card {
          id
          title
        }
      }
    }
    """