import pygame
from src.snake.entities.entity import Entity
from src.snake.input.direction_input import DirectionInput
from pygame import Surface


class Score(Entity):
    def __init__(self, value: int = 0) -> None:
        self._value = value
        self._font = pygame.font.Font(None, 36)

    @property
    def value(self) -> int:
        return self._value

    def increase(self, inc: int = 1) -> None:
        self._value += inc

    def update(self, direction_input: DirectionInput | None = None) -> None:
        pass

    def render(self, surface: Surface) -> None:
        score_text = self._font.render(f"Score: {self._value}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))
