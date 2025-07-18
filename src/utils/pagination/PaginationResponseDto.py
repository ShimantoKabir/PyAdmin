from dataclasses import dataclass

@dataclass
class PaginationResponseDto[T]:
  items: list[T]
  total: int