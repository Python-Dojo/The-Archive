# Create a Grid
GRID_HEIGHT = 12
GRID_WIDTH = 10
N = 1
S = 2
W = 4
E = 8

GRID = {}
for y in range(GRID_HEIGHT):
  GRID[y] = {}
  for x in range(GRID_WIDTH):
    GRID[y][x] = 15
    # print(f'GRID[{y}][{x}] = {GRID[y][x]}')

# Define rules for maze

# Assume that the entrance and exit are on the top left and bottom right?
GRID[0][0] = " "
GRID[GRID_HEIGHT - 1][GRID_WIDTH - 1] = " "

# Draw the outline


# Break Wall Function
def breakWall(y, x, dir):
  if dir == 'N':
    # Check if possible
    GRID[x][y] = GRID[x][y] - 1
    GRID[x][y + 1] = GRID[x][y + 1] - 2
    # Repeat for other directions
  if dir == 'S':
    GRID[x][y] = GRID[x][y]
    GRID[x][y] = GRID[x][y]

  if dir == 'W':
    GRID[x][y] = GRID[x][y]
    GRID[x][y] = GRID[x][y]
  if dir == 'E':
    GRID[x][y] = GRID[x][y]
    GRID[x][y] = GRID[x][y]


# Implement Sidewinder Algorythm
# https://weblog.jamisbuck.org/2011/2/3/maze-generation-sidewinder-algorithm

# Plot maze
# ╋ ┳ ┻ ┫ ┣ ┛ ┏ ┗ ┓ ┃ ⚊
for row in GRID:
  # col_str = f"{row}: "
  col_str = ""
  for col in GRID[row]:
    symbol = "╋"
    if row == 0:
      symbol = "┳"
      if col == 0:
        symbol == "┏"
      elif col == GRID_WIDTH - 1:
        symbol == "┓"
    elif row == GRID_HEIGHT - 1:
      symbol = "┻"
      if col == 0:
        symbol == "┗"
      elif col == GRID_WIDTH - 1:
        symbol == "┛"
    else:
      if col == 0:
        symbol == "┣"
      elif col == GRID_WIDTH - 1:
        symbol == "┫"

    col_str = col_str + symbol
  print(col_str)
