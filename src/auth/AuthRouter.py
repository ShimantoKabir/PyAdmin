from fastapi import APIRouter
from src.auth.dtos.LoginResponseDto import LoginResponseDto
from src.auth.dtos.LoginRequestDto import LoginRequestDto
from di import AuthServiceDep
from src.auth.dtos.AuthRefreshResponseDto import AuthRefreshResponseDto
from src.auth.dtos.AuthRefreshRequestDto import AuthRefreshRequestDto

routes = APIRouter()

@routes.post("/auth/login", response_model=LoginResponseDto, tags=["auth"])
async def login(loginRequestDto: LoginRequestDto, authService: AuthServiceDep) -> LoginResponseDto:
  return authService.login(loginRequestDto)

@routes.post("/auth/refresh", response_model=AuthRefreshResponseDto, tags=["auth"])
async def refresh(authRefreshRequestDto: AuthRefreshRequestDto, authService: AuthServiceDep) -> AuthRefreshResponseDto:
  return authService.refresh(authRefreshRequestDto)
  
  
