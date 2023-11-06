import random
import string
from point import Point
from direction import Direction


class WordGrid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.initialise_word_grid()

    def __str__(self):
        return self.get_stringified_word_grid()


    def initialise_word_grid(self):
        self.word_grid = [[" " for col in range(
            self.cols)] for row in range(self.rows)]

    def get_stringified_word_grid(self) -> str:
        output = ""
        for row in self.word_grid:
            for char in row:
                output += char + " "
            output += "\n"
        return output

    def read_line(
        self, position: Point, orientation: Direction, length: int
    ) -> str | None:
        result = ""

        current_row, current_col = position
        next_row, next_col = orientation
        grid_rows = len(self.word_grid)
        grid_cols = len(self.word_grid[0])

        for i in range(length):
            if not 0 <= current_row < len(self.word_grid):
                return None

            if not 0 <= current_col < len(self.word_grid[0]):
                return None

            result += self.word_grid[current_row][current_col]
            current_row += next_row
            current_col += next_col

        return result

    def write_line(self, position: Point, orientation: Direction, data: str) -> bool:
        can_write_line = self.read_line(position, orientation, len(data))
        if not can_write_line:
            return False

        current_row, current_col = position
        next_row, next_col = orientation

        for char in data:
            self.word_grid[current_row][current_col] = char
            current_row += next_row
            current_col += next_col

        return True

    def fill_blank_space(self):
        for row_index, row in enumerate(self.word_grid):
            for col_index, char in enumerate(row):
                if char == " ":
                    self.word_grid[row_index][col_index] = random.choice(
                        string.ascii_uppercase
                    )
