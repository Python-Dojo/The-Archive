# Task

Build a playable, two-player version of Connect Four for the terminal.

Connect Four is played on a seven-column, six-row board. Players take turns dropping a coloured piece into a column; the piece occupies the lowest available position. The first player to make a line of four horizontally, vertically, or diagonally wins.

## What the program does

The implementation is in `Group-1/main.py`. It defines a `Connect4` class that stores the board, tracks whose turn it is, accepts moves, displays the board, and checks for a winner.

The board is represented as a six-by-seven list of cells. `make_play()` places the current player's piece at the bottom of the selected column, or directly above the existing pieces. `do_user_move()` prompts for a column numbered 1 through 7 and asks again if the input is invalid or the chosen column is full.

After each move, the game switches players and prints the updated board. `check_victory()` searches every row, column, and diagonal for four consecutive red or blue pieces. When it finds a winner, the game prints the winning piece.

## Main concept

The central idea is to represent the board as a matrix, then check all possible winning lines. The `columns` property transposes the row-based board, and `diagonals` builds diagonal sequences in both slopes. The same consecutive-four check can then be applied to each direction.

The game loop continues until a winning line is found:

1. Prompt the current player for a column.
2. Place the piece if the move is legal.
3. Switch turns and display the board.
4. Check for four matching pieces in a row, column, or diagonal.

## Output

The program displays the board in the terminal using red and blue circle symbols. It repeatedly prompts for moves and updates the board until a player connects four pieces, then prints a win message.

The current implementation does not detect a draw if the board fills without a winner.

## Summary

This project is a compact, interactive Connect Four game. It covers board representation, input validation, gravity-based piece placement, turn-taking, and win detection across horizontal, vertical, and diagonal lines. The result is a playable terminal game, with draw handling left as a possible extension.
