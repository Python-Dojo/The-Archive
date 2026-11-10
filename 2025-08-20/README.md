# Task

Build an “Idea Vault”: a command-line tool for saving, categorising, listing, and deleting project ideas.

## What the program does

The implementation is in `Group-2/main.py`. It creates a SQLite database named `idea_vault.db` with tables for ideas, categories, and links between ideas and categories.

The script uses `argparse` to provide three commands:

- `add` saves an idea, with optional person and comma-separated categories
- `list` prints the saved ideas
- `delete` removes an idea by its database ID

The `insert_value()` function inserts the idea, creates category records when needed, and associates category IDs with the new idea. `list_values()` currently prints the basic idea rows; it does not display their category associations.

## Main concept

The project combines a small command-line interface with a relational database. Ideas and categories are stored separately, with a linking table to represent the many-to-many relationship: one idea can have several categories, and a category can be used by many ideas.

The command parser dispatches each requested action to the corresponding database operation. The database is created if its tables do not already exist, allowing the tool to retain ideas between runs.

## Output

The `list` command prints the rows stored in the `ideas` table. The `add` and `delete` commands update the SQLite database; the script does not yet provide polished confirmation messages or category-aware listing.

The prototype has unfinished edges: category handling and deletion are not fully robust, and the argument parser does not require the categories option even though the add path expects a category string. It is an exploratory CLI rather than a finished idea-management application.

## Summary

This session's project is a persistent idea notebook built from `argparse` and SQLite. It demonstrates basic CRUD operations and a relational model for tagging ideas, with the intended result being a growing, searchable-by-extension idea store. Listing and category management are still minimal and could be developed further.
