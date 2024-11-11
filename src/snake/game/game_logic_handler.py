import pygame
import random

from src.snake.entities.score import Score
from src.snake.entities.grid import Grid
from src.snake.entities.food import Food
from src.snake.entities.snake import Snake
from src.snake.grid_renderer.point import Point


class GameLogicHandler:
    def __init__(self, grid: Grid, snake: Snake, food: Food, score: Score) -> None:
        self._grid = grid
        self._snake = snake
        self._food = food
        self._score = score

    def handle(self) -> None:
        # check if eats food
        if self._snake.head_pos == self._food.pos:
            all_cells = set(Point(x, y) for y in range(self._grid.config.height) for x in range(self._grid.config.width))
            for cell in self._snake.pos:
                all_cells.remove(cell)
            self._food.respawn(random.choice(list(all_cells)))
            self._snake.grow()
            self._score.increase()

        # collision check
        if (self._snake.head_pos in self._snake.pos[1:]
                or self._snake.head_pos.x < 0 or self._snake.head_pos.y < 0
                or self._snake.head_pos.x >= self._grid.config.width or self._snake.head_pos.y >= self._grid.config.height):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def get_score(self) -> int:
        return self._score.value
