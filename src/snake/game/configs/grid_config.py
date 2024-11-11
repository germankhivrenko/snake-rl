from dataclasses import dataclass


@dataclass(frozen=True)
class GridConfig:
    width: int = 16
    height: int = 16
    cell_size: int = 32
    bg_color = (218, 112, 214)  # orchid
    grid_color = (255, 255, 255)  # white
    gutter_size = 2

    @property
    def width_px(self) -> int:
        return self.height * self.cell_with_gutter_size + self.gutter_size

    @property
    def height_px(self) -> int:
        return self.height * self.cell_with_gutter_size + self.gutter_size

    @property
    def cell_with_gutter_size(self) -> int:
        return self.cell_size + self.gutter_size
