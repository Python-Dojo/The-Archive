# Task

Implement Conway's Game of Life and display its generations as a terminal animation.

The Game of Life is a cellular automaton played on a grid. Each cell is either alive or dead, and the next state of every cell is determined by the number of its eight surrounding neighbours.

## What the program does

The implementation in `Group-1/main.py` creates a random starting board using `init_grid()`. It then repeatedly calculates the next generation with `make_next_frame()` and prints the evolving board for 70 iterations.

The board is represented by the `Grid` class in `Group-1/grid.py` as a 30-by-30 list of Boolean values. `count_neighbours()` counts the live cells around a given row and column, while `set_alive()` and `kill()` update individual cells. `print()` renders live cells as `X` and dead cells as blank spaces.

At each step, the program applies the standard Game of Life rules:

- A live cell survives when it has two or three live neighbours.
- A live cell dies with fewer than two neighbours or more than three.
- A dead cell becomes alive when it has exactly three live neighbours.

## Main concept

Each generation is computed from the previous generation, not by changing cells in place. `make_next_frame()` reads the old grid and writes the outcomes into a new one. This matters because every cell's fate should be based on the same snapshot of the board.

The board treats cells beyond its edges as dead. The initial board is random, so different runs can produce different patterns and evolution.

## Output

The program clears the terminal, prints the current grid, and pauses briefly between generations to create an animation. The archived `Group-1/Conway.gif` demonstrates the intended visual result.

The folder also includes `e2e_test.py`, an unfinished test file; its trailing incomplete function definition means it is not currently a runnable test suite.

## Summary

This project is a small terminal implementation of Conway's Game of Life. It demonstrates a two-dimensional grid, neighbour counting, generation-by-generation state updates, and simple terminal animation. Its output is an evolving pattern of live and dead cells rather than a fixed solution.
