from fastapi import APIRouter
from src.auth.dtos.LoginResponseDto import LoginResponseDto
from src.auth.dtos.LoginRequestDto import LoginRequestDto
from di import AuthServiceDep

routes = APIRouter()

@routes.post("/auth/login", response_model=LoginResponseDto, tags=["auth"])
async def login(loginRequestDto: LoginRequestDto, authService: AuthServiceDep) -> LoginResponseDto:
  return authService.login(loginRequestDto)
  