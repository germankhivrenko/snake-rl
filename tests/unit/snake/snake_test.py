import pytest
from src.snake.entities.snake.direction_states.direction_state import DirectionStates
from src.snake.grid_renderer.point import Point
from src.snake.entities.snake import Snake


@pytest.mark.parametrize(
    "state, expected_pos",
    (
        (DirectionStates.upward_state, [Point(5, 5), Point(5, 4), Point(5, 3)]),
        (DirectionStates.rightward_state, [Point(5, 5), Point(4, 5), Point(3, 5)]),
        (DirectionStates.downward_state, [Point(5, 5), Point(5, 6), Point(5, 7)]),
        (DirectionStates.leftward_state, [Point(5, 5), Point(6, 5), Point(7, 5)]),
    )
)
def test_init_pos(state, expected_pos):
    snake = Snake(
        head_pos=Point(5, 5),
        size=3,
        direction_state=state,
    )

    assert snake._pos == expected_pos
