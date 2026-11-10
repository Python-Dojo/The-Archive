# Task

Create a generator for a Hashiwokakero-style logic puzzle.

Hashiwokakero is a number-placement puzzle where islands are connected by bridges. Each island has a number indicating how many bridges it must connect to, no more than two bridges can be placed between any two islands, and bridges cannot cross islands or other bridges. The goal is to form a connected network of bridges that satisfies every island's required total.

This folder contains a prototype from the 2024-09-18 Bristol Python Dojo session. It is not a polished or complete game engine, but it captures the core data model and the general structure of a puzzle generator.

## What the program does

The code in `Group-1/main.py` defines a basic set of classes meant to represent a puzzle board:

- `Island`: stores the island's coordinates and required bridge count
- `Bridge`: stores a connection between two islands
- `Grid`: stores islands, bridges, used positions, and the maximum allowed bridge distance
- `Hashiwokakero`: the main puzzle generator/controller

At the start of the file, the author describes the rules of the puzzle in comments and outlines the preferred design. The code then creates a coordinate-based system for placing islands and checking possible bridge routes.

The main design idea is to model the board as a graph-like structure: islands are nodes, bridges are edges, and a generated puzzle is valid when every island satisfies its number of connections without violating the puzzle's geometric rules.

## Main concept

The central concept is not a finished puzzle generator, but a board model that can reason about valid neighbours and possible bridge placements.

The relevant part is the `valid_neighbours()` method on `Grid`:

```python
for dx, dy in DIRECTIONS:
    x, y = island.x, island.y
    for dist in range(1, self.max_dist):
        pos = (x + dx * dist, y + dy * dist)
        if pos not in self.used:
            valid.append(pos)
        else:
            break
        if pos in self.island_positions:
            break
```

This means the script is trying to identify which positions are legal next steps from an island when placing bridges. It only allows movement in four directions (up/down/left/right), and it stops once it reaches:

- an occupied island position
- a used bridge position
- or the maximum allowed distance

That is a good fit for a puzzle generator because the validity of a bridge depends on local geometry.

The file also includes a comment block that describes the intended generation process:

- pick a random island
- compute all reachable legal positions from it
- randomly choose a valid next position
- add the bridge or island connection
- repeat until the desired board size or island count is reached

This is the general strategy the session was exploring: a random, incremental puzzle construction process that gradually builds a valid Hashiwokakero board.

## The output and intended result

The intended output is a valid Hashiwokakero board: a set of numbered islands connected by bridges such that each island has the correct number of total connections and the full board forms a single connected system.

The code's data model clearly points toward this output:

- islands are placed at coordinates
- bridges are tracked as connections between two islands
- `used` coordinates prevent the same path from being reused badly
- `max_dist` limits how far a bridge may reach before the board becomes invalid

The puzzle generation approach is therefore aiming to produce a clean and playable network of islands rather than simply printing a random grid.

## Why this is useful

Even though the script is incomplete, it captures the key rules and a realistic approach to solving the problem:

- model islands and bridges as structured data
- use coordinates to keep placement valid
- constrain bridge lengths and crossings
- plan generation as a process of adding connected elements instead of a blind random fill

This is a good example of a game-generation prototype: it is not yet the final puzzle engine, but it has the right building blocks.

## Summary

This project is a rough prototype for generating Hashiwokakero puzzles. It models islands, bridge connections, board geometry, and legal neighbour detection, and it is designed around the rule that every island must be connected to the correct number of bridges without violating board constraints.

The code is intentionally incomplete and more of a concept sketch than a finished generator, but it shows the right approach for the task: represent the puzzle as a graph of coordinates and connections, then build the board incrementally while respecting the puzzle rules.

The real output the project is aiming for is a valid, playable puzzle board with numbered islands connected by valid bridges.
