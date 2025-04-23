import os
from dotenv import load_dotenv

load_dotenv(".env.dev")

def get_env_val(key : str) -> str :
  return os.environ.get("DB_URL")





