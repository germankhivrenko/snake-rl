from src.snake.grid_renderer.point import Point
from src.snake.input.direction_input import DirectionInput
from src.snake.entities.snake.direction_states.direction_state import DirectionState


class LeftwardState(DirectionState):
    @staticmethod
    def get_prev_pos_delta() -> Point:
        return Point(x=1)

    @staticmethod
    def get_next_pos_delta() -> Point:
        return Point(x=-1)

    def handle_input(self, direction_input: DirectionInput) -> DirectionState:
        from src.snake.entities.snake.direction_states import DirectionStates

        if direction_input == DirectionInput.UP:
            return DirectionStates.upward_state
        if direction_input == DirectionInput.DOWN:
            return DirectionStates.downward_state
        return self
