from dataclasses import dataclass

@dataclass
class UpdateUserResponseDto:
  id: int
  disabled: bool
  super: bool
  firstName: str
  lastName: str
  contactNumber: str