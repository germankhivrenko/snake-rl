import pygame.draw
from pygame import Surface

from src.snake.input.direction_input import DirectionInput
from src.snake.entities.snake.direction_states.direction_state import DirectionState
from src.snake.entities.snake.direction_states import DirectionStates
from src.snake.entities.grid import GridConfig
from src.snake.grid_renderer.point import Point
from src.snake.entities.scene import Entity


class Snake(Entity):
    DEFAULT_SIZE = 5
    DEFAULT_COLOR = (211, 211, 211)
    DEFAULT_SPEED = 8  # frames per move

    def __init__(
            self,
            grid_config: GridConfig,
            head_pos: Point | None = None,
            size: int = DEFAULT_SIZE,
            direction_state: DirectionState = DirectionStates.upward_state,
            speed = DEFAULT_SPEED,
    ) -> None:
        head_pos = head_pos if head_pos else Point(x=grid_config.width // 2, y=grid_config.height // 2)
        prev_pos_delta = direction_state.get_prev_pos_delta()

        self._grid_config = grid_config
        self._pos = [head_pos + (i * prev_pos_delta) for i in range(size)]
        self._state = direction_state
        self._prev_tail_pos = self._pos[-1] + self._state.get_prev_pos_delta()
        self._last_updated_state = self._state
        self._speed = speed
        self._frames_counter = 0

    @property
    def head_pos(self) -> Point:
        return self._pos[0]

    @property
    def pos(self) -> list[Point]:
        return self._pos

    def grow(self) -> None:
        self._pos.append(self._prev_tail_pos)

    def update(self, direction_input: DirectionInput | None = None) -> None:
        if direction_input:
            # TODO: might not be the best name
            new_state = self._state.handle_input(direction_input)
            self._last_updated_state = new_state if new_state != self._state else self._last_updated_state

        if self._frames_counter == self._speed:
            self._state = self._last_updated_state
            # update body
            self._prev_tail_pos = self._pos[-1]
            for i in range(len(self._pos) - 1, 0, -1):
                self._pos[i] = self._pos[i - 1]
            # update head
            self._pos[0] = self._pos[0] + self._state.get_next_pos_delta()
            self._frames_counter = 0
        else:
            self._frames_counter += 1


    def render(self, surface: Surface) -> None:
        for point in self._pos:
            self._render_cell(surface, point)

    def _render_cell(self, surface: Surface, point: Point) -> None:
        # if (point.x < 0 or point.x >= self._grid_config.width
        #     or point.y < 0 or point.y >= self._grid_config.height):
        #     # TODO: consider more elegant way since the last render is not quite good
        #     return

        x_offset = (surface.get_width() - self._grid_config.width_px) // 2
        y_offset = (surface.get_height() - self._grid_config.height_px) // 2

        x = x_offset + point.x * self._grid_config.cell_with_gutter_size + self._grid_config.gutter_size
        y = y_offset + point.y * self._grid_config.cell_with_gutter_size + self._grid_config.gutter_size
        cell_size = self._grid_config.cell_size

        pygame.draw.rect(surface, self.DEFAULT_COLOR, rect=(x, y, cell_size, cell_size))
