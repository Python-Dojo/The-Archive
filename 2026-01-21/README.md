# Task

Convert a grid of mine locations into a Minesweeper-style board by displaying a mine marker for each mine and the adjacent-mine count for every other cell.

## What the programs do

The session contains two attempts.

`Group-2/radnom_mines.py` is the more complete implementation. `make_mine_grid()` creates a random grid with a configurable size and mine ratio. `do_the_thing()` walks the grid, prints a bomb emoji for mine cells, and counts mines in the eight surrounding positions for safe cells. It uses coloured terminal escape codes to style the numbers.

`Group-1/main.py` starts from a fixed 10-by-10 example grid and sketches helpers for checking bounds and counting neighbouring mines. It is unfinished and contains import, indexing, and syntax errors, so it does not currently produce the intended board.

`Group-2/test_main.py` includes a sample grid and imports the random generator; `results.txt` preserves a sample output. The `Group-2/main.py` file only prints the sample grid constant and current directory, rather than running the renderer.

## Main concept

For each cell, examine the eight surrounding offsets (including diagonals), ignore coordinates outside the grid, and count how many of the remaining cells contain mines. The displayed value is the local mine count; mine cells themselves remain marked as mines.

The random grid and the rendered board are separate stages: one chooses mine locations, while the other derives the visible numbers from those locations.

## Output

Running `Group-2/radnom_mines.py` prints the generated Boolean-like grid, followed by a Minesweeper-style text board with bombs and adjacent-mine counts. The sample layout changes on each run because mine positions are selected randomly.

This is a display prototype, not a playable game: it does not accept reveals, track flags, or detect wins and losses.

## Summary

This project generates a random minefield and computes the neighbouring-mine counts needed to display a Minesweeper board. Group 2 provides the functioning core; Group 1 records an incomplete attempt at the same grid-neighbour problem.
