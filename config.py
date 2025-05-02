import os
from dotenv import load_dotenv

load_dotenv(".env.dev")

class Config:
  def getValByKey(key: str) -> str:
    return os.environ.get(key)





