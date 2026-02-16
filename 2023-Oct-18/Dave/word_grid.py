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

    def is_valid_line(self, position: Point, direction: Direction, length: int) -> bool:
        initial_row_index = position.row
        initial_col_index = position.col
        max_row_index = len(self.grid) - 1
        max_col_index = len(self.grid[0]) - 1

        # A single character would have length 1 but no motion, hence multiplying
        # the direction amount by length - 1
        total_row_motion = direction.row * (length - 1)
        total_col_motion = direction.col * (length - 1)

        final_char_row_index = initial_row_index + total_row_motion
        final_char_col_index = initial_col_index + total_col_motion

        if (
            final_char_row_index > max_row_index
            or final_char_row_index < 0
            or final_char_col_index > max_col_index
            or final_char_col_index < 0
        ):
            return False

        return True

    def read_line(self, position: Point, direction: Direction, length: int) -> str:
        if not self.is_valid_line(position, direction, length):
            raise GridOverflowError()

        result = ""

        current_row, current_col = position
        next_row, next_col = direction

        for i in range(length):
            result += self.grid[current_row][current_col]
            current_row += next_row
            current_col += next_col

        return result

    def write_line(self, position: Point, direction: Direction, data: str) -> bool:
        if not self.is_valid_line(position, direction, len(data)):
            raise GridOverflowError()

        current_row, current_col = position
        next_row, next_col = direction

        for char in data:
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
