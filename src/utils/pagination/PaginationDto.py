from dataclasses import dataclass

@dataclass
class PaginationDto:
  first: int
  rows: int
  page: int