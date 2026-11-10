# Tasks

This session contains two separate command-line programming exercises: a to-do list manager and a solver for the Countdown numbers game.

## What the programs do

### Group 1: JSON-backed to-do list

`Group-1/main.py` sketches a command-line to-do app. It defines helpers to load and save JSON data and uses `argparse` subcommands for adding, completing, and editing items. Tasks are intended to be stored in `todolist.json` as a mapping from task text to a completion flag.

This version is incomplete: the command handling does not correctly implement all of the declared subcommands, and its load fallback hides read/parse errors by replacing the data with a placeholder item. It demonstrates the command-line and JSON-storage idea but is not yet a reliable task manager.

### Group 2: Countdown numbers solver

`Group-2/main.py` generates six numbers from the standard small- and large-number pools, chooses a random three-digit target, and recursively explores arithmetic expressions using the selected numbers. It uses addition, subtraction, multiplication, and integer division, and requires divisions to be exact.

The recursive search combines pairs of numbers into parenthesised expressions and continues until one expression remains. If that expression equals the target, it prints the expression and value.

## Main concepts

The to-do prototype explores parsing subcommands and persisting simple application state as JSON.

The Countdown solver explores recursive search: at each step, choose two available values, combine them with a legal operation, and search again with the result replacing those values. Parentheses preserve the operation order in the expression being built.

## Output

The to-do app is intended to add, mark complete, rename, or delete tasks in a JSON file, but its current command flow does not complete those actions correctly.

The Countdown script prints a randomly generated target and six numbers, followed by any arithmetic expressions it finds that reach the target. It can be computationally expensive because it searches many combinations, and the script returns matching expressions rather than reporting a nearest result when no exact solution is found.

## Summary

The archive for this date preserves two unrelated prototypes. Group 1 explores a JSON-backed to-do CLI, while Group 2 searches for Countdown arithmetic solutions. One focuses on basic command parsing and persistence; the other on recursive combinatorial search. Both are session work in progress rather than polished applications.
