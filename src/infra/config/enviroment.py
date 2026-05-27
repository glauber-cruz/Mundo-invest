from os import getenv
from dotenv import load_dotenv

ENV = getenv("ENV", "dev")

def load_enviroment():
  match ENV:
    case "test":
      load_dotenv(".env.test")
    case "prod":
      load_dotenv(".env.prod")
    case "dev":
      load_dotenv(".env")
    case _:
      raise ValueError(f"Invalid environment: {ENV}")

load_enviroment()