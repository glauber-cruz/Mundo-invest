from enum import Enum


class ClientStatus(str, Enum):
    WAITING_ANALYSIS = "Aguardando Análise"
    PROCESSED = "Processado"


class ClientPriority(str, Enum):
    HIGH = "prioridade_alta"
    NORMAL = "prioridade_normal"
