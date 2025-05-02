from fastapi import APIRouter

routes = APIRouter()

@routes.get("/users/{id}", tags=["user"])
async def getById(id: int):
  return id