# base case - horizontal and vertical only

# have a list of words

# randomly pick some words

class WordSearch:

  def __init__(self, width: int, height: int, words: list[str]):
    self.words = words
    self.width = width 
    self.height = height
    self.grid: list[list[str]] = []
    self.generate_empty_grid()

    # test data
    self.grid[1][1] = "c"
    self.grid[1][2] = "o"
    self.grid[1][3] = "w"

  def generate_empty_grid(self):
      self.grid = [["" for _ in range(self.width)] for _ in range(self.height)]

# take word and current grid and search for all legal positions and number of intersections

  def is_valid_position(self, word: str, row: int, column: int) -> dict[str, int]:
    """Find if the word is valid horizontally or vertically
    output dict of {"h": _, "v": _} if horizontal and vertical are valid and have intersections, otherwise {} empty dict means invalid
    """

    result = {}

    # check for horizontal intersections
    horizontal_intersections = 0
    if column + len(word) <= self.width:
      for (index, letter) in enumerate(word):
        grid_letter = self.grid[row][column + index]
        if grid_letter == "":
          continue
        elif grid_letter != letter:
            horizontal_intersections = None
            break
        elif grid_letter == letter:
            horizontal_intersections += 1  

    # check for vertical intersections
    vertical_intersections = 0
    if row + len(word) <= self.height:
      for (index, letter) in enumerate(word):
        grid_letter = self.grid[row + index][column]
        if grid_letter == "":
            continue
        elif grid_letter != letter:
            vertical_intersections = None
            break
        elif grid_letter == letter:
            vertical_intersections += 1

    result["h"] = horizontal_intersections if horizontal_intersections is not None
    result["v"] = vertical_intersections if vertical_intersections is not None

    return result
      

  def try_get_best_position(self, word: str) -> tuple[int, int, int] | None:
    """Finds the position with the most intersections, and returns it along with whether its horizontal or vertical"""
    results: dict[tuple[int, int, str], int] = {}
    length = len(word)
    for y in range(self.height):
      if y + length > self.height: 
        break
      for x in range(self.width):
        if x + length >= self.width:
          break
        # check if valid to have word in position (x, y)
        if position := self.is_valid_position(word, y, x):
          if (h := position.get("h")) is not None:
            results[(x, y, "h")] = h
          if (v := position.get("v")) is not None:
            results[(x, y, "v")] = v
    if results:
      return max(results, key=results.get)

  def get_best_position(self, word: str) -> tuple[int, int, int]:
    """keep increasing the grid until a position is valid"""
    while not (position := self.try_get_best_position(word)):
      # if the word can't be placed, make grid bigger
      self.height += 1
      self.width += 1
      for g in self.grid:
        g.append("")
      self.grid.append(["" for _ in range(self.width)])
    return position

  def place_word(self, word: str) -> None:
    """Get the best position and place word on the grid"""
    x, y, direction = self.get_best_position(word)
    for i, w in enumerate(word):
      if direction == "h":
        self.grid[y][x + i] = w
      elif direction == "v":
        self.grid[y + i][x] = w

  def main(self) -> None:
    """sort the list in size decreasing order to hopefully minimise grid size"""
    sorted_words = sorted(self.words, key=len, reverse=True)
    # comment
    for word in sorted_words:
      self.place_word(word)
    self.display_grid()

  def display_grid(self) -> None:
    """print rows from self.grid"""
    for row in self.grid:
      print("".join(row))
    


# mainloop - for each new word, get the intersections, if any are valid, then pick randomly one with the most intersections
# otherwise, expand the grid

# place word in grid

# print out grid nicely

# Example of intersection-tracking grid
# [
#    [(h: 0, v: 1), (h: 0, v: 0), (h: 0, v: 0)],
#    [(h: 1, v: 0), None , (h: 0, v: 0)],
#    [(h: 0, v: 1), (h: 1, v: 0), (h: 0, v: 1)],
# ]
# {
# (0, 0): { "h": 1 }
# (0, 1): { "v": 0 }
# (0, 2): { "h": 1, "v": 1 }
# } 
#
#

if __name__ == "__main__":
  words = ["cat", "dog", "bird", "mouse", "fish"]
  word_search = WordSearch(width = 18, height = 12, words = words)
  # word_search.display_grid()
  print(word_search.is_valid_position(word = "cow", row = 1, column = 1))
