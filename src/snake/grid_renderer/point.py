from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return self + (-other)

    def __mul__(self, scalar: int) -> "Point":
        return Point(scalar * self.x, scalar * self.y)

    def __rmul__(self, scalar: int) -> "Point":
        return self * scalar

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
