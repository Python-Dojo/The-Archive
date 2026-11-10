# Task

Generate and print every fixed-orientation polyomino of a requested size. A polyomino is a shape made from connected unit squares joined edge-to-edge.

The challenge description in `Group-1/main.py` asks for shapes up to size six, with rotations treated as distinct orientations. It gives the expected counts for sizes one through six: 1, 2, 6, 19, 63, and 216.

## What the program does

The script represents each square by integer `(x, y)` coordinates. Starting from a single square, `generate(n)` recursively takes every shape of size `n - 1`, adds a new square beside each existing square, and normalises the resulting coordinates so the top-left extent starts at zero. A set removes duplicate coordinate sets produced by different growth paths.

`Polyomino.__repr__()` renders a shape as rows of `#` characters and spaces. When run directly, the program asks for a size and prints the generated shapes, separated by blank lines, along with a count.

## Main concept

The generator builds shapes incrementally. Every new square is placed in one of the four cardinal directions from an existing square, so the resulting shape remains edge-connected. Coordinate normalisation removes duplicates that differ only by translation.

Rotations and reflections are not normalised against one another. That is why the requested counts distinguish orientations, while shapes in different positions on the infinite grid still count as the same shape.

## Output

Enter a positive size when prompted. The program prints a text drawing for every generated shape and reports the number of unique coordinate configurations.

Generation is cached by size, but the number of shapes grows quickly. The challenge description's totals provide a useful check for sizes one through six.

## Summary

This project is a recursive polyomino enumerator. It models shapes as sets of grid coordinates, grows them by attaching one square at a time, removes translation duplicates, and prints each orientation as ASCII art.
