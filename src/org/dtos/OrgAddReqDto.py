from dataclasses import dataclass
from typing import List
from pydantic import HttpUrl, constr, field_validator

@dataclass
class OrgAddReqDto:
  name: constr(min_length=1) # type: ignore
  domain: constr(min_length=1) # type: ignore
  websites: List[HttpUrl]

  @field_validator('websites')
  def validateWebsites(cls, values: List[HttpUrl]) -> List[HttpUrl]:
    if not isinstance(values, list):
      raise TypeError("Websites must be a list")
    if not all(isinstance(v, HttpUrl) for v in values):
      raise ValueError("All items in websites must be HttpUrl")
    return values