
from enum import Enum
from dataclasses import dataclass

PIXEL_SIZE = 4
PIXEL = (PIXEL_SIZE, PIXEL_SIZE)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


@dataclass
class Physics:
    velocity: list
    acceleration: list
    position: list
