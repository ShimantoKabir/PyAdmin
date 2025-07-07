from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateUserRequestDto:
  disabled: Optional[bool] = None # Not required
  super: Optional[bool] = None # Not required
  firstName: Optional[str] = None  # Not required
  lastName: Optional[str] = None  # Not required
  contactNumber: Optional[str] = None  # Not required