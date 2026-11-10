# Task

Implement a word-chain game in which players take turns choosing unused dictionary words that begin with the last letter of the previous word.

## What the programs do

`Group-1/the_good_version.py` contains the playable prototype. It loads lowercase, non-plural entries from a word-list file passed on the command line, chooses a random starting word for the CPU, and alternates between user input and a CPU-selected word. A valid next word must begin with the previous word's final letter. The CPU chooses randomly from the remaining matching words; if none remain, the user wins.

`Group-1/the_bad_code.py` is an earlier attempt to put the dictionary and word selection into a class. It shuffles a word list and removes words as they are selected, but the code refers to an undefined base class and has incomplete or incorrect game logic.

The accompanying `words.txt` provides the dictionary data used by the game.

## Main concept

The game is a turn-based chain constrained by word boundaries: each next word must start with the previous word's last character. Keeping track of used words prevents the CPU from repeating its own choices. The word list supplies the finite set of possible moves, so the game can end when the current player has no valid continuation.

## Output and limitations

Run the prototype with a dictionary file:

```bash
python the_good_version.py words.txt
```

The program prints the CPU's current word, prompts for the user's next word, and eventually prints either a loss message with a score or `You win!`. In the current implementation, the score is never incremented, user words are checked for the starting-letter rule but not verified against the dictionary, and repeated user words are not rejected. The result is a simple game prototype rather than a fully validated word-chain implementation.

## Summary

This project turns a dictionary into a lightweight word-chain game with a random CPU opponent. It demonstrates file-based word loading, legal-move filtering, random selection, and a basic game loop. The good-version script captures the intended experience, while input validation and scoring remain incomplete.
