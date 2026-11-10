# Task

Transform a short piece of text into a playful, less predictable version by replacing words with synonyms and selected letters with visually similar characters.

## What the program does

The code in `Group-1/main.py` uses NLTK's WordNet corpus to find synonyms for each word in a sample Markdown passage. It then applies a regular expression to substitute selected Latin letters with accented or lookalike characters. Random choices make the output vary between runs.

`get_similar_words()` gathers synonyms from WordNet, and `do_replacements()` processes the input and returns the altered text. The script also includes a small example of using a regular-expression replacement callback to uppercase matched text. `katie.py` contains a similar experiment with the same general idea.

## Main concept

The project combines lexical substitution with character-level obfuscation:

1. Split the input into words and ask WordNet for alternatives.
2. Replace words when synonyms are available.
3. Use a regular expression callback to swap selected characters for similar-looking Unicode characters.

The result is intended to feel like a quirky “new year” text generator, while demonstrating `re.sub()` callbacks, randomness, and a lexical database.

## Output and limitations

Running the script prints a few demonstrations and then transformed versions of the sample Markdown. WordNet must be installed and its corpus data available locally.

The code is an unfinished experiment and has syntax/runtime problems in the character replacement function; several `match` cases return malformed values or are incomplete. WordNet may also return no synonyms for a token or synonyms that do not fit the surrounding phrase. As archived, the script is not expected to produce a reliable transformed passage without fixes.

## Summary

This session explores a text mutation tool that mixes dictionary-based synonym replacement with random Unicode lookalikes. Its intended output is a playful, altered version of input text; the archived code captures the idea but needs repair before it can run consistently.
