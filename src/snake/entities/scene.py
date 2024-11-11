from typing import Sequence
from abc import ABC

from pygame import Surface

from src.snake.input.direction_input import DirectionInput


class Entity(ABC):
    def update(self, direction_input: DirectionInput | None) -> None:
        ...

    def render(self, surface: Surface) -> None:
        ...


class Scene(Entity):
    def __init__(self, enities: Sequence[Entity] | None = None) -> None:
        self._entities = list(enities) if enities else []

    def add_entity(self, entity: Entity) -> None:
        self._entities.append(entity)

    def update(self, direction_input: DirectionInput | None) -> None:
        for entity in self._entities:
            entity.update(direction_input)

    def render(self, surface: Surface) -> None:
        for entity in self._entities:
            entity.render(surface)
