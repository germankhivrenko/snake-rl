from src.snake.game.configs.game_loop_config import GameLoopConfig
from src.snake.game.configs.grid_config import GridConfig
from src.snake.game.game_logic_handler import GameLogicHandler
from src.snake.game.game_loop import GameLoop
from src.snake.entities.snake import Snake
from src.snake.entities.food import Food
from src.snake.entities.grid import Grid
from src.snake.entities.score import Score
from src.snake.entities.scene import Scene
from pygame import Surface
from src.snake.grid_renderer.point import Point


class GameFactory:
    def __init__(self, surface: Surface) -> None:
        self._game_loop_config = GameLoopConfig()
        self._grid_config = GridConfig()
        self._surface = surface

    def create(self) -> GameLoop:
        grid = Grid(self._grid_config)
        snake = Snake(self._grid_config)
        food = Food(self._grid_config, Point(x=2, y=2))  # TODO: hardcoded
        score = Score()

        scene = Scene()
        scene.add_entity(grid)
        scene.add_entity(snake)
        scene.add_entity(food)
        scene.add_entity(score)

        game_logic_handler = GameLogicHandler(grid, snake, food, score)

        return GameLoop(
            config=self._game_loop_config,
            scene=scene,
            surface=self._surface,
            game_logic_handler=game_logic_handler,
        )

    def _create_scene(self) -> Scene:
        grid = Grid(self._grid_config)
        snake = Snake(self._grid_config)
        food = Food(self._grid_config, Point(x=2, y=2))  # TODO: hardcoded
        score = Score()

        scene = Scene()
        scene.add_entity(grid)
        scene.add_entity(snake)
        scene.add_entity(food)
        scene.add_entity(score)

        return scene
