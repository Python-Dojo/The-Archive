
from __future__ import annotations
from dataclasses import dataclass

from typing import TypeAlias

"""Hashiwokakero Generator
Rules
- Connect islands (the circles with numbers) with as many bridges as the number in the island.
- There can be no more than two bridges between two islands.
- Bridges cannot go across islands or other bridges.
- The bridges will form a continuous link between all the islands.

I don't like the idea of an adjancency matrix:
    - some nodes will required multiple edges
    - it won't account for georgraphical constraints
"""

Coord: TypeAlias = tuple[int, int]

CHAR_SETS = [
    ["-", "="], # horizontal
    ["|", "║"] # vertical
]

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

@dataclass
class Island:
    x: int
    y: int
    value: int

    @property
    def position(self) -> Coord:
        return self.x, self.y


@dataclass
class Bridge:
    start: Island
    end: Island

    def __str__(self):
        return f"{self.start.x},{self.start.y} -> {self.end.x},{self.end.y}"

@dataclass
class Grid:
    islands: list[Island]
    bridges: list[Bridge]
    used: list[tuple[int, int]] # coordinates used in bridges
    max_dist: int

    @property
    def island_positions(self):
        return [island.position for island in self.islands]

    def valid_neighbours(self, island: Island) -> list[Coord]:
        valid: list[Coord] = []
        for dx, dy in DIRECTIONS:
            x, y = island.x, island.y
            for dist in range(1, self.max_dist):
                pos = (x + dx * dist, y + dy * dist)
                if pos not in self.used:
                    valid.append(pos)
                else:
                    break
                if pos in self.island_positions:
                    break # can't go further
        return valid
    
# @dataclass
class Hashiwokakero:
    """General Idea:
    Provide a number of islands and max distance between them
    At each iteration, pick a random island, and get all the available positions that can be moved to from it
    Pick one at random, and add it with a line
    Repeat until max islands reached
    """
    grid:Grid

    def __init__(self, islands: int, max_island_distance: int = 3) -> None:
        self.max_islands = islands
        self.max_dist = max_island_distance
        self.invalid_positions = []
        self.islands = []

    def generate(self):
        """Randomly generate a Haskiwokakero puzzle"""
        weight = rand(1, 10)
        direction = rand(0, 4)
        count = rand(0, 2)
        island = Island()

        for(island in self.gridslands)
        if(!self.grid.hasCollision(bridge)) {
            self.grid.addIsland()
        }        
     



        ...
