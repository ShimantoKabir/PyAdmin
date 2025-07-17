from fastapi import APIRouter
from core import app, getAllRoutes

routes = APIRouter()

@routes.post("/actions", tags=["actions"])
async def get()-> list[str]:
  return getAllRoutes()
  