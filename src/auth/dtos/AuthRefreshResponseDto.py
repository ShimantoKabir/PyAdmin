from dataclasses import dataclass

@dataclass
class AuthRefreshResponseDto:
  accessToken: str
  refreshToken: str