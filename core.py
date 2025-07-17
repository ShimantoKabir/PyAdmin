from fastapi import FastAPI

app = FastAPI()

def getAllRoutes() -> list[str]:
  routes : list[str] = []
  for route in app.routes:
    if route.name and str(route.name).startswith("act:"):
      routes.append(route.name)
  return routes

@app.get("/",tags=["health"])
async def test()->str:
  return "App is running.....!"