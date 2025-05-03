"""maze generator"""
# Generate Empty maze
# Add in and out - top left bottom right
# Gernerate outline
# Generate walls ⬛⬜

# w#######
# # ⬜
# # ⬜⬛⬛⬛
# ⬛⬛⬛
# +-+-+-+-+-+
# |         |
# +-+-+-+ +-+
# |     | | |
# + +-+-+ + +
# |         |
# +-+ +-+-+-+
import sys
from random import shuffle

sys.setrecursionlimit(5000)

PATH = "⬜"
WALL = "⬛"
WIDTH = 43
HEIGHT = 43

class MazeGenerator:
    """Maze Generator :)"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.maze: list[list[int]] = []

    def generate_maze(self):
        self.reset()
        row, col = 1, 1
        self.recursive_break_walls(row, col)

    def public_print(self) -> None:
        for row in range(HEIGHT):
            for col in range(WIDTH):
                print(WALL if self.maze[row][col] == 1 else PATH, end="")
            print()

    def reset(self) -> None:
        """
        Make an empty maze
        Each cell has a left and top wall
        """
        self.maze = [[1 for row in range(self.width)]
                     for height in range(self.height)]
        self.maze[0][1] = 0
        self.maze[self.width-1][self.height-2] = 0

    def recursive_break_walls(self, row: int, col: int) -> None:
        """recursively visit cells and make a path"""
        nbrs = [(row + 2, col), (row - 2, col), (row, col - 2), (row, col + 2)]
        valid_nbrs = [
            n for n in nbrs
            if 0 < n[0] < self.height - 1 and 0 < n[1] < self.width - 1
        ]
        shuffle(valid_nbrs)
        for nbr in valid_nbrs:
            if self.maze[nbr[0]][nbr[1]] != 0:
                self.break_wall(row, col, *nbr)
                self.recursive_break_walls(nbr[0], nbr[1])

    def break_wall(self, start_row: int, start_col: int, end_row, end_col):
        if start_row < end_row:
            for row in range(start_row, end_row + 1):
                self.maze[row][start_col] = 0
        elif start_row > end_row:
            for row in range(end_row, start_row + 1):
                self.maze[row][start_col] = 0
        elif start_col < end_col:
            for col in range(start_col, end_col + 1):
                self.maze[start_row][col] = 0
        elif start_col > end_col:
            for col in range(end_col, start_col + 1):
                self.maze[start_row][col] = 0


def main() -> None:
    """main proc"""
    maze_gen = MazeGenerator(width=WIDTH, height=HEIGHT)
    maze_gen.generate_maze()
    maze_gen.public_print()


if __name__ == "__main__":
    main()
