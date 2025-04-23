from fastapi import FastAPI
from src.user import UserRouter

app = FastAPI()
app.include_router(UserRouter.routes)

@app.get("/")
async def test()->str:
  return "App is running.....!"

