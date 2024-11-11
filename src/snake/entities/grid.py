from dataclasses import dataclass

import pygame
from pygame import Surface

from src.snake.input.direction_input import DirectionInput
from src.snake.entities.scene import Entity
from src.snake.game.configs.grid_config import GridConfig


class Grid(Entity):
    def __init__(self, config: GridConfig) -> None:
        self._config = config

    @property
    def config(self) -> GridConfig:
        return self._config

    def update(self, direction_input: DirectionInput | None) -> None:
        pass

    def render(self, surface: Surface) -> None:
        surface.fill(self._config.bg_color)

        assert surface.get_width() >= self._config.width_px
        assert surface.get_height() >= self._config.height_px

        x_offset = (surface.get_width() - self._config.width_px) // 2
        y_offset = (surface.get_height() - self._config.height_px) // 2
        end_x = x_offset + self._config.width_px - 1 # self._config.gutter_size
        end_y = y_offset + self._config.height_px - 1 # self._config.gutter_size

        for i in range(self._config.width + 1):
            x = x_offset + i * self._config.cell_with_gutter_size
            pygame.draw.line(
                surface,
                self._config.grid_color,
                start_pos=(x, y_offset),
                end_pos=(x, end_y),
                width=self._config.gutter_size,
            )
        for i in range(self._config.height + 1):
            y = y_offset + i * self._config.cell_with_gutter_size
            pygame.draw.line(
                surface,
                self._config.grid_color,
                start_pos=(x_offset, y),
                end_pos=(end_x, y),
                width=self._config.gutter_size,
            )
