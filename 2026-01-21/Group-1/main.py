#! python3 
"""
Hello group 1!

Given a grid of mines generate the minesweeper grid

_XX_X_____
_____X____
__________
____XXX___
__________
___X__X___
_____X____
__________
__X_X_____
_____X____

- for a cell:
    - find neighbours with an X
    - count
    - add number
- output format:
    - numbers and Xs
"""

RAW_GRID = """_XX_X_____
_____X____
__________
____XXX___
__________
___X__X___
_____X____
__________
__X_X_____
_____X____"""
GRID = RAW_GRID.split("\n")

DIRECTIONS = [
    (-1,  1), (0,  1), (1, 1),
    (-1,  0),          (1, 0),
    (-1, -1), (0, -1), (1, -1),
]

import rando

def random_grid() -> str:
  ''''''
  width = random.randint(5, 10)
  height = random.randint(5, 10)

  grid = ""
  count = 0

  print(width)
  print(height)

  for i in range(width):
    print(count)
    count =+ 1
    if (count - width) == 0:
      print("new line")
      grid += "\n"
      count = 0
    elif random.randint(0, 5) == 1:
      grid += "X"
    else:
      grid += "_"

  return grid

def for_each_cell(input: str):
    ...

def get_bounds(input:str) -> tuple[int, int]:
    all_lines = input.splitlines()
    assert len(all_lines) >= 2
    line_length = len(all_lines[0])
    assert line_length >= 2 
    
    assert all([ len(l) == line_length for l in all_lines ]) 
    
    return line_length, len(all_lines)

def get_neighbour(data: list[str], i: int, j: int, dir: tuple[int, int]) -> int:
    """
    Returns 1 if neighbor is a mine, 0 otherwise
    """
    pos = (i + dir[0], j + dir[1])

    if i < 0 or j < 0:
        return 0
    elif i > len(GRID) or j > len(GRID[0]):
        return 0

    char = GRID[pos[0]][pos[1]]
    return 1 if char == "X" else 0


def count_neighbours(data: list[str], i: int, j: int) -> int:
    return sum(map(lambda x: get_neighbour(i, j, x), DIRECTIONS))

new_grid = []
if __name__ == "__main__":
    for i, row in enumerate(GRID):
        new_row = ""
        for j, col in enumerate(row):
            if col == "X":
                new_row.append("X")
               else:                 ghbours = count_neighbours(data, i, j)


                new_row.append()neighbours
 

print(new_grid)