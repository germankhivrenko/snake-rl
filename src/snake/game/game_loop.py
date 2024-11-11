from dataclasses import dataclass
import pygame
from pygame import Surface

from src.snake.input.direction_input import DirectionInput
from src.snake.entities.scene import Entity
from src.snake.game.game_logic_handler import GameLogicHandler
from src.snake.game.configs.game_loop_config import GameLoopConfig
import time


class GameLoop:
    def __init__(self, config: GameLoopConfig, scene: Entity, surface: Surface, game_logic_handler: GameLogicHandler) -> None:
        self._config = config
        self._scene = scene
        self._surface = surface
        self._running = False
        self._prev_iter_ms = _get_current_time_ms()
        self._curr_iter_ms = _get_current_time_ms()
        self._elapsed_ms = 0
        self._lag_ms = 0
        self._game_logic_handler = game_logic_handler
        pygame.init()
        pygame.font.init()

    def run(self) -> int:
        # Returns score

        self._running = True
        self._prev_iter_ms = _get_current_time_ms()
        while self._running:
            self._iterate()
        return self._game_logic_handler.get_score()


    def _iterate(self):
        self._curr_iter_ms = _get_current_time_ms()
        self._elapsed_ms = self._curr_iter_ms - self._prev_iter_ms
        self._prev_iter_ms = self._curr_iter_ms
        self._lag_ms += self._elapsed_ms

        direction_input = self._process_input()

        while self._lag_ms >= self._config.ms_per_frame:
            self._update(direction_input)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

        if self._running:
            self._render()

            diff_ms = _get_current_time_ms() - self._curr_iter_ms
            to_wait_ms = (self._config.ms_per_frame - diff_ms) / 1000
            if to_wait_ms > 0:
                time.sleep(to_wait_ms)

    def _process_input(self) -> DirectionInput | None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return DirectionInput.UP
                elif event.key == pygame.K_RIGHT:
                    return DirectionInput.RIGHT
                elif event.key == pygame.K_DOWN:
                    return DirectionInput.DOWN
                elif event.key == pygame.K_LEFT:
                    return DirectionInput.LEFT
        return None

    def _update(self, direction_input: DirectionInput | None) -> None:
        self._scene.update(direction_input)
        self._game_logic_handler.handle()
        self._lag_ms -= self._config.ms_per_frame

    def _render(self) -> None:
        self._scene.render(self._surface)
        pygame.display.flip()


# TODO: to utils
def _get_current_time_ms() -> int:
    return time.time_ns() // 1000000

