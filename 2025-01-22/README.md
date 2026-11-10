# Task

Build a helper for Wordle-style puzzle solving by filtering candidate words based on what the player already knows.

This folder contains a Python prototype from the 2025-01-22 session. The goal is to take guesses and feedback, then reduce the set of possible valid answers until there is only one candidate left. This is a classic Wordle deduction problem.

## What the program does

The script in `Group-1/main.py` sets up the structure for a Wordle helper.

It starts by loading a word list from `words.txt`:

```python
def _get_words():
    with open("words.txt", "r") as file:
        return file.read().split()
```

It then defines:

- `CharState`: an enum for the three feedback states
  - `Incorrect`
  - `Wrong_Location`
  - `Correct`
- `WordleGuess`: a helper object that stores a guessed word and the feedback pattern

The script also includes a `validation_guess()` function that validates guesses in the format:

```text
ABCDE 00000
```

where:

- the first token is the guessed word
- the second token is a 5-character score string using 0/1/2-style states

The program then loops through user input, records guesses, and tries to narrow down candidate answers with `get_suggestions()`.

## Main concept

The central concept is candidate elimination.

For each guess, the system receives information about whether each letter is:

- not in the word
- in the word but in the wrong place
- in the correct place

The code is designed around that idea, even though the actual filtering logic is still a stub.

At the moment, `get_suggestions()` is incomplete:

```python
def get_suggestions(guesses: list[WordleGuess]) -> list[str]:
    return ["wordl"]
```

and `step(...)` is also not implemented. That means the project is a partial solver rather than a fully working Wordle assistant.

## Output

The expected output is a list of possible remaining words after each guess. The script is meant to prompt for a guess, validate it, and then print likely candidates until only one remains.

This makes the session’s output more like an interactive solver or word filter than a pure static utility.

## Summary

This project is a Wordle brainstorming tool in its early stages. It shows the right data structures and user flow for a word-guessing helper, but the actual logic to eliminate candidates is still unfinished. The session was clearly exploring a solver pattern: store the guess history, evaluate letter states, and narrow down the set of valid answers step by step.

The code is useful as a scaffold for a Wordle assistant, even though it does not yet fully implement the filtering algorithm.
