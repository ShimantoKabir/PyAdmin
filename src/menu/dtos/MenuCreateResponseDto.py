from dataclasses import dataclass

@dataclass
class MenuCreateResponseDto:
  id: int
  label: str
  icon: str
  href: str