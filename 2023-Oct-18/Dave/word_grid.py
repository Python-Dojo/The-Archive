import random
import string
from point import Point
from direction import Direction
from exceptions import GridOverflowError


class WordGrid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.initialise_grid()

    def __str__(self):
        return self.get_stringified_word_grid()

    def initialise_grid(self):
        grid = []

        for row in range(self.rows):
            grid_row = []
            for col in range(self.cols):
                grid_row.append(" ")
            grid.append(grid_row)

        self.grid = grid

    def get_stringified_word_grid(self) -> str:
        output = ""
        for row in self.grid:
            row_string = " ".join(row)
            output += f"{row_string}\n"
        return output

    def check_for_grid_overflow(self, row: int, col: int) -> None:
        if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]):
            raise GridOverflowError()

    def read_line(self, position: Point, direction: Direction, length: int) -> str:
        result = ""

        current_row, current_col = position
        next_row, next_col = direction

        for i in range(length):
            self.check_for_grid_overflow(current_row, current_col)
            result += self.grid[current_row][current_col]
            current_row += next_row
            current_col += next_col

        return result

    def write_line(self, position: Point, direction: Direction, data: str) -> bool:
        current_row, current_col = position
        next_row, next_col = direction

        for char in data:
            self.check_for_grid_overflow(current_row, current_col)
            self.grid[current_row][current_col] = char
            current_row += next_row
            current_col += next_col

        return True

    def fill_blank_space(self):
        for row_index, row in enumerate(self.grid):
            for col_index, char in enumerate(row):
                if char == " ":
                    self.grid[row_index][col_index] = random.choice(
                        string.ascii_uppercase
                    )
