from dataclasses import dataclass
from point import Point
from direction import Direction


@dataclass
class Placement:
    position: Point
    direction: Direction

    def __iter__(self):
        yield self.position
        yield self.direction
