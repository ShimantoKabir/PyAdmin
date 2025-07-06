from dataclasses import dataclass
from typing import List
from pydantic import HttpUrl

@dataclass
class OrgAddResDto:
  id: int
  name: str 
  domain: str
  websites: List[HttpUrl]