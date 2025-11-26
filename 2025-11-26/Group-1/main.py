"""
A polyomino is a 2D shape formed by joining squares along common edges, 
    such that all squares are connected. 
    
Output each possible polyomino (including every rotation), 
    up to a size of 6, 
    in any order. 

Separate each polyomino by an empty line.

There should be a total of 
    1 monomino,     #
    2 dominoes,     ## (and rotated) 
    6 trominoes,
    19 tetrominoes,
    63 pentominoes,
    and 216 hexominoes.
"""

from __future__ import annotations

from functools import cache
from typing import NamedTuple, Sequence
from dataclasses import dataclass

@dataclass
class Vector:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Vector) -> Vector:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other: Vector) -> Vector:
        self.x -= other.x
        self.y -= other.y
        return self



def normalise_coords(*coords: tuple[Vector]) -> frozenset[Vector]:
    """adjust coords to a 0,0 base"""
    min_x = min(c.x for c in coords)
    min_y = min(c.y for c in coords)
    return frozenset({c - Vector(min_x, min_y) for c in coords})

@dataclass(frozen=True)
class Polyomino:
    coords: frozenset[Vector]

    def __repr__(self):
        """Adjust to a (0,0) smallest, and then put hashes in coord positions"""
        norm = self.coords
        max_x = max(c.x for c in norm)
        max_y = max(c.y for c in norm)
        grid = [[" " for col in range(max_x+1)]for col in range(max_y+1)]
        for c in norm:
            grid[c.y][c.x] = "#"
        return "\n".join("".join(map(str, row)) for row in reversed(grid))

moves = [Vector(-1, 0), Vector(0, -1), Vector(1, 0), Vector(0, 1)] 

def is_valid(move: Vector, poly: Polyomino) -> bool:
    ...

@cache
def generate(n: int) -> set[Polyomino]:
    """Generate each polyomino and return the list"""
    if n == 1:
        return {
            Polyomino((Vector(0, 0),))
        }
    else:
        previous = generate(n-1)
        result: set[Polyomino] = set()

        for poly in previous:
            for coord in poly.coords:
                for move in moves:
                    new_coord = coord + move
                    if new_coord not in poly.coords:
                        result.add(Polyomino(coords=normalise_coords(*poly.coords, new_coord)))
        return result
        
    
def print_polyominos(to_print : Sequence[Polyomino]):
    string_reprs = {str(p) for p in to_print}
    print(f"{len(string_reprs)=} == {len(to_print)=}")
    assert len(string_reprs) == len(to_print)
    for p in to_print : print(p, end="\n\n")
    print(len(to_print))


if __name__ == "__main__":
    n = int(input("What rank? "))
    # n = 8
    print_polyominos(generate(n))


