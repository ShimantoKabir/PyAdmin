from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
from config import get_env_val

engine = create_engine(get_env_val("DB_URL"),echo=True)

def get_session():
  with Session(engine) as session:
    yield session

DBSessionDep = Annotated[Session, Depends(get_session)]