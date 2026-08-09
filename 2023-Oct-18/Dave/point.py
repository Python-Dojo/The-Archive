from dataclasses import dataclass


@dataclass
class Point:
    row: int
    col: int

    # This allows us to unpack a point with the syntax:
    # row, col = point
    def __iter__(self):
        yield self.row
        yield self.col
