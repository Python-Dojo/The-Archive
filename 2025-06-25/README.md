# Task

Create a small command-line file viewer that lists the current directory's contents with visual markers for files, folders, and symbolic links.

## What the program does

The main implementation is in `Group-1/main.py`. It gets the current working directory, lists its entries, and prints one line for each item:

- files are shown with a note icon
- directories are shown with a folder icon
- symbolic links include their target and a link icon

The helper functions use `os` to identify each entry and build its display text. For links to paths containing directories, the output shortens the target to its final path component.

The folder also includes `notMain.py`, another version of the directory viewer, and `VeryNotMain.py`, a separate shell configuration experiment that loads decoded values from a local shared environment file into shell environment variables.

## Main concept

The program is a simple presentation layer over filesystem metadata. It distinguishes entry types, formats a concise label for each one, and prints the current directory as a flat list. The comments describe possible future additions such as sorting, grouping by extension, and drawing a directory tree, but those features are not implemented.

## Output

Running `main.py` prints the entries in the process's current working directory, one per line, annotated with an emoji. It does not recurse into subdirectories or render a tree.

## Summary

This session's Python program is a lightweight terminal directory listing with friendlier visual labels. It demonstrates basic filesystem inspection and string formatting, while leaving sorting, recursive traversal, and a fuller ASCII-art display as future ideas.
