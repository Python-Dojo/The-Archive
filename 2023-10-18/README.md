# Task

Create a word-search-style grid generator that places a list of words in a rectangular grid while trying to maximise overlaps between words.

This folder contains a small Python prototype built during the Bristol Python Dojo session on 2023-10-18. The core idea is to place words either horizontally or vertically, use the letter overlap as a scoring signal, and expand the grid when no valid placement is currently possible.

## What the program does

The program defines a `WordSearch` class that manages:

- a grid of characters
- a list of target words
- placement logic for words in the grid
- scoring of valid positions based on intersections
- printing the final word-search layout

The solution is not a full polished word-search generator. It is more of a working prototype that explores how to place words in a matrix with shared letters, which is the key challenge in making a crossword-like puzzle.

## The main concept

The key challenge is deciding where to put each word.

A valid placement is one where:

- the word fits inside the current grid
- it does not contradict letters already placed on the board
- it aligns either horizontally or vertically
- it keeps the number of matching intersections as high as possible

The code tries to score each candidate position using the number of letters that already match when placed in a row or column.

## Important parts of the code

### `WordSearch.__init__`

The constructor stores:

- `words`: the list of words to place
- `width` and `height`: the current grid dimensions
- `grid`: a 2D list of strings used to represent the board

It also creates an empty grid and sets a tiny test pattern in the middle of it:

```python
self.grid[1][1] = "c"
self.grid[1][2] = "o"
self.grid[1][3] = "w"
```

This is a demonstration that the board can already contain some starting letters, making it easy to test overlap and validation logic.

### `generate_empty_grid`

This creates a blank board with empty strings for every cell:

```python
self.grid = [["" for _ in range(self.width)] for _ in range(self.height)]
```

This gives a mutable grid that can be expanded or filled as words are placed.

### `is_valid_position`

This is the most important method in the class.

It checks whether a word can be placed at a given `(row, column)` in either of two directions:

- horizontal: `row` stays the same, letters extend across columns
- vertical: `column` stays the same, letters extend down rows

For each direction it checks every letter in the word:

- if the cell is empty, there is no conflict and it effectively does not count as an intersection
- if the cell already contains the same letter, that is a valid overlap and increments the count
- if the cell contains a different letter, the placement is invalid

It returns a dictionary like:

```python
{"h": 2, "v": 1}
```

where the values are the numbers of matching intersections in each direction. If a direction is invalid, it leaves that key out of the result.

### `try_get_best_position`

This method searches the whole board for possible placements and records the best intersection score for each candidate.

It loops through each cell and checks whether a word could fit there. If it can, it stores the best score for that direction in a dictionary keyed by `(x, y, direction)`.

At the end it picks the placement with the highest score:

```python
return max(results, key=results.get)
```

This effectively chooses the location that maximises overlap with existing letters, which is a good heuristic for creating a compact, connected word search.

### `get_best_position`

If no valid position can be found at the current size, the grid is expanded:

```python
self.height += 1
self.width += 1
```

This is a simple but practical strategy: when the board becomes too tight, it grows one row and one column larger until the word fits.

### `place_word`

Once a best position is chosen, the word is written into the grid:

- horizontally: fill cells from left to right
- vertically: fill cells from top to bottom

### `main`

The `main` method sorts the words by length, longest first, and then places each word in turn.

This ordering is sensible because longer words are usually harder to fit and should be placed before shorter ones. That reduces the chance of getting stuck later.

### `display_grid`

This prints the grid as a simple string-based board.

## Example usage

The script includes an example in the bottom of the file:

```python
if __name__ == "__main__":
  words = ["cat", "dog", "bird", "mouse", "fish"]
  word_search = WordSearch(width = 18, height = 12, words = words)
  print(word_search.is_valid_position(word = "cow", row = 1, column = 1))
```

This does not fully run the word-placement algorithm in the `__main__` block; instead, it demonstrates validation by checking whether `"cow"` fits into the test grid at `(1, 1)`.

## How it behaves in practice

The algorithm is a simple heuristic-based approach:

1. sort words by length descending
2. try each word in the current board
3. find the best valid legal position with the most intersections
4. if no position is valid, grow the board
5. place the word
6. repeat until all words are placed

This is a useful way to build a crossword-like layout without requiring a more advanced backtracking solver.

## Strengths of this prototype

- clear concept of placement and overlap scoring
- simple, readable Python implementation
- uses grid expansion when necessary
- good demonstration of how word placement heuristics can work

## Limitations

This is still a prototype and not a robust puzzle generator.

Some limitations include:

- only horizontal and vertical placements are allowed
- no diagonal or reverse-order placements
- the search is not full backtracking, so some word combinations may produce poor layouts or fail unexpectedly
- the script is designed as a toy example rather than a production-ready word-search engine

## Running it

From this folder, run:

```bash
python "main.py"
```

This will execute the example code and print the validation result for the test placement, while also providing a basic demonstration of the class and grid logic.

## Summary

This project is a compact exploration of how to place words into a grid using overlap heuristics. It is a nice example of a small algorithmic challenge: given a list of words, find good positions that fit the board and share letters where possible. The code is intentionally simple and educational rather than fully generalised.
