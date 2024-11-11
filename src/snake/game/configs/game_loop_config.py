from dataclasses import dataclass


@dataclass(frozen=True)
class GameLoopConfig:
    ms_per_frame: int = 16
