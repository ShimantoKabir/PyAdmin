from dataclasses import dataclass

@dataclass
class LoginResponseDto:
  accessToken: str
  refreshToken: str