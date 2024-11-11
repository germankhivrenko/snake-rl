from src.snake.grid_renderer.point import Point
from src.snake.input.direction_input import DirectionInput
from src.snake.entities.snake.direction_states.direction_state import DirectionState


class DownwardState(DirectionState):
    @staticmethod
    def get_prev_pos_delta() -> Point:
        return Point(y=-1)

    @staticmethod
    def get_next_pos_delta() -> Point:
        return Point(y=1)

    def handle_input(self, direction_input: DirectionInput) -> DirectionState:
        from src.snake.entities.snake.direction_states import DirectionStates

        if direction_input == DirectionInput.RIGHT:
            return DirectionStates.rightward_state
        if direction_input == DirectionInput.LEFT:
            return DirectionStates.leftward_state
        return self
