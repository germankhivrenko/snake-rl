from abc import ABC
from pygame import Surface


class Entity(ABC):
    def update(self) -> None:
        ...

    def render(self, surface: Surface) -> None:
        ...