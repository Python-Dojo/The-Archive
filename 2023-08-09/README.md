# Task

Mastermind is a classic code-breaking board game where one player creates a secret sequence and the other player tries to guess it. This script implements a simple terminal version of that game in Python.

The computer generates a hidden sequence of characters, the player selects a difficulty level, and then tries to guess the sequence. After each guess, the program gives feedback using black and white pegs:

- black peg: the character is correct and in the correct position
- white peg: the character is correct but in the wrong position

The valid character set is taken from the alphabet and digits:

ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789

The game asks for a difficulty choice, validates the guess length and characters, scores each guess, and declares victory once the full answer has been guessed correctly.

This is a lightweight prototype of the game and is intended as a quick exercise in Python logic, input validation, and simple game design.

To run it:

```bash
python "Mastermind boardgame.py"
```
