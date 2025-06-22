from typing import Protocol, runtime_checkable

Number = int | float


@runtime_checkable
class Ordered(Protocol):
    def __lt__(self, other: "Ordered") -> bool: ...
