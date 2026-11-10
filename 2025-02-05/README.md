# Task

Create a small helper that prints neatly formatted tables using custom ASCII borders and column widths.

This folder contains a Python utility from the 2025-02-05 dojo session. The script focuses on a simple but useful formatting problem: taking a list of column names and values, then rendering them in a consistent table layout with border characters and padded cells.

## What the program does

The implementation in `Group-1/main.py` defines three main functions:

- `create_line(column_names, fill_character="*", spacings=None)`
- `fill_line(length, fill_character="*")`
- `get_headers_from_csv(file)`

These functions are used to build a neatly aligned table around a CSV-like header row.

The main logic is:

```python
def create_line(column_names:list[str], fill_character:str = "*", spacings:list[int]|None = None):
    if spacings is None:
        spacings = [7] * len(column_names)
    padded_columns = [str(c).center(w) for c, w in zip(column_names, spacings)]
    return f'{fill_character} {f" {fill_character} ".join(padded_columns)} {fill_character}'
```

This creates a line of a table where each column is centered and separated by the chosen fill character.

The script also includes a sample `main()` that reads headers from a CSV file and prints a simple table layout to the terminal.

## Main concept

The central concept is formatting rather than computation.

The program is trying to turn raw data into a visual, readable output by:

- padding strings to fixed widths
- joining cells with separators
- repeating border characters to frame each row
- centering labels inside column widths

This is a classic data-display task: create a table that is readable even when the content lengths vary.

The code is intentionally simple but effective as a strong example of how to produce CLI-friendly table formatting without using a heavy library.

## Output

The output is a nicely framed ASCII table in the terminal, like a custom-made report or dashboard layout.

The code includes a test block at the end that checks that the formatting functions behave correctly, including:

- default fill characters
- custom fill characters
- column padding and border generation

This means the program is both a formatter and a tiny validation script for the formatting behavior.

## Summary

This project is a small utility for rendering readable ASCII tables. It is focused, practical, and easy to understand: given a list of column names and dimensions, it generates a styled border line and a simple report-like layout. The value is not in complex computation but in clean output design for command-line tools.

It is a very good example of a dojo challenge where the real work is not about business logic, but about formatting data so it is easier to read and present.
