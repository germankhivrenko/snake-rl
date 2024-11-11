import random

from dataclasses import dataclass
import pygame
from pygame import Surface

from src.snake.game.game_factory import GameFactory
from src.snake.input.direction_input import DirectionInput
from src.snake.entities.grid import Grid, GridConfig
from src.snake.grid_renderer.point import Point
from src.snake.entities.scene import Scene, Entity
from src.snake.entities.snake import Snake
from src.snake.entities.food import Food
import time


MS_PER_FRAME = 16  # ~60 FPS


def _get_current_time_ms() -> int:
    return time.time_ns() // 1000000


# TODO:
# 1. [Done] Score -> Entity
# 2. Event bus for entities
#   2.1. Food respawn
#   2.2. Collision check
# 3. while running -> GameLoop
# 4. Grid renderer


# class Score(Entity):
#     def __init__(self, value: int = 0) -> None:
#         self._value = value
#         self._font = pygame.font.Font(None, 36)
#
#     def increase(self, inc: int = 1) -> None:
#         self._value += inc
#
#     def update(self, direction_input: DirectionInput) -> None:
#         pass
#
#     def render(self, surface: Surface) -> None:
#         score_text = self._font.render(f"Score: {self._value}", True, (255, 255, 255))
#         surface.blit(score_text, (10, 10))
#
# @dataclass(frozen=True)
# class GameLoopConfig:
#     ms_per_frame: int = 16


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Snake")

    game_factory = GameFactory(screen)
    game = game_factory.create()

    score = game.run()
    print(f"You scored: {score}!")


if __name__ == '__main__':
    main()
