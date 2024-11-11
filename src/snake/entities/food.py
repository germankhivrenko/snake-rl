import pygame
from pygame import Surface

from src.snake.input.direction_input import DirectionInput
from src.snake.entities.grid import GridConfig
from src.snake.grid_renderer.point import Point
from src.snake.entities.scene import Entity


class Food(Entity):
    DEFAULT_COLOR = (255, 255, 255)

    def __init__(self, grid_config: GridConfig, pos: Point) -> None:
        self._grid_config = grid_config
        self._pos = pos

    @property
    def pos(self) -> Point:
        return self._pos

    def respawn(self, pos: Point) -> None:
        self._pos = pos

    def update(self, direction_input: DirectionInput | None) -> None:
        pass

    def render(self, surface: Surface) -> None:
        # TODO: remove duplicate offset calc
        x_offset = (surface.get_width() - self._grid_config.width_px) // 2
        y_offset = (surface.get_height() - self._grid_config.height_px) // 2

        half_cell_size = self._grid_config.cell_size / 2
        x = x_offset + self._pos.x * self._grid_config.cell_with_gutter_size + self._grid_config.gutter_size + half_cell_size
        y = y_offset + self._pos.y * self._grid_config.cell_with_gutter_size + self._grid_config.gutter_size + half_cell_size

        pygame.draw.circle(surface, self.DEFAULT_COLOR, center=(x, y), radius=half_cell_size - 1)

