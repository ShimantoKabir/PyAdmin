from fastapi import FastAPI
from src.user import UserRouter
from src.menu import MenuRouter

app = FastAPI()
app.include_router(UserRouter.routes)
app.include_router(MenuRouter.routes)

@app.get("/")
async def test()->str:
  return "App is running.....!"

