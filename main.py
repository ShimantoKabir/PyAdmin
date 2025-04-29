from fastapi import FastAPI
from src.user import UserRouter
from src.menu import MenuRouter
from src.auth import AuthRouter

app = FastAPI()
app.include_router(UserRouter.routes)
app.include_router(MenuRouter.routes)
app.include_router(AuthRouter.routes)

@app.get("/")
async def test()->str:
  return "App is running.....!"

