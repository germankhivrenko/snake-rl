from abc import ABC

from src.snake.input.direction_input import DirectionInput
from src.snake.grid_renderer.point import Point


class DirectionState(ABC):
    @staticmethod
    def get_prev_pos_delta() -> Point:
        ...

    @staticmethod
    def get_next_pos_delta() -> Point:
        ...

    def handle_input(self, direction_input: DirectionInput) -> "DirectionState":
        ...
