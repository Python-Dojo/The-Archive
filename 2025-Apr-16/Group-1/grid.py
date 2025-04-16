
from typing import Iterable
from copy import deepcopy

GRID_SIZE:int = 30

class Grid:
    """
    store a 2d thing (list of lists is fine)
    """
    GRID_SIZE = 30

    def __init__(self):
        self._grid: list[list[bool]] = [ deepcopy([False] * GRID_SIZE ) for _ in range( GRID_SIZE) ]

    def get_grid(self) -> Iterable[Iterable[bool]]:
        return self._grid
    
    def is_alive(self, i, j):
        return self._grid[i][j]


    def count_neighbours(self, target_row: int, target_col: int):
        neighbors = []
        for x, row in enumerate(self._grid):
            for y, elem in enumerate(row):
                if x == target_row and abs(y - target_col) == 1:
                    neighbors.append(elem)
                elif abs(x - target_row) == 1 and abs(y-target_col) <= 1:
                    neighbors.append(elem)
        return sum(neighbors)

    def get_neighbours(self, target_row: int, target_col: int):
        """
        Get the king move neighboards given a 2d cell position
        """
        neighbors = []
        for x, row in enumerate(self._grid):
            for y, elem in enumerate(row):
                neighbors.append(elem)
                if x == target_row and abs(y - target_col) == 1:
                    neighbors.append((x, y))
                elif abs(x - target_row) == 1 and abs(y-target_col) <= 1:
                    neighbors.append((x, y))

        return neighbors
                    
    def print(self):
        """
        loop over rows in _grid and print
         ` ` for dead `#` for alive
        """
        for i in range(0, GRID_SIZE):
            for j in range(0, GRID_SIZE):
                if self._grid[i][j]:
                    print("X", end="")
                else:
                    print(" ", end="")
            print("")
    
    def set_alive(self, i, j):
        self._grid[i][j] = True
    
    def kill(self, i, j):
        self._grid[i][j] = False
        
if __name__ == "__main__":
    grid = Grid()
    print(grid)