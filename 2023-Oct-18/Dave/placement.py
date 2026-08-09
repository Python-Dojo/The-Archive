from dataclasses import dataclass
from point import Point
from direction import Direction


@dataclass
class Placement:
    position: Point
    direction: Direction

    # This allows us to unpack a placement with the syntax:
    # position, direction = placement
    def __iter__(self):
        yield self.position
        yield self.direction
