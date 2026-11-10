# Task

Generate random project ideas and turn them into short, playful, pseudo-creative "dojo challenge" prompts.

This folder contains work from the 2024-10-30 Bristol Python Dojo session, where the goal was to generate funny, synthetic task descriptions using random nouns, verbs, and sentence templates. The result is a lightweight idea generator that produces phrases like:

> Dojo, today you must invent a royal that bites a sense

The code is a fun example of procedural text generation: combine random words from curated lists to create absurd but usable challenge prompts.

## What the program does

The core implementation is in `Group-1/main.py`.

It reads word lists from the `text/` directory:

- `nouns.txt`
- `verbs.txt`
- `make_synonyms.txt`
- `transitive_verbs.txt`

These are loaded with a helper function:

```python
def read_text(filename: str) -> list[str]:
    return Path(DATA_PATH, f"{filename}.txt").read_text().splitlines()
```

It then selects words at random from those lists to assemble a sentence pattern.

The important structure is the `QuantumWord` and `QuantumNounWithArticle` classes. These are wrappers around a list of words and choose one randomly when rendered:

```python
class QuantumWord:
    def __init__(self, words: list[str]) -> None:
        self.words = words

    def __str__(self):
        return select_word(self.words)
```

`QuantumNounWithArticle` adds an article (`"a"` or `"an"`) before the noun, choosing based on the first letter of the word.

The final output is produced by `main()`:

```python
def main():
    q_a_noun = QuantumNounWithArticle(NOUNS)
    m_verb = QuantumWord(MAKE_VERBS)
    t_verb = QuantumWord(TRANS_VERBS)
    return f"Dojo, today you must {m_verb} {q_a_noun} that {t_verb}s {q_a_noun}"
```

This creates a pseudo-random sentence that reads like a deliberately awkward challenge specification.

## Main concept

The main concept is lexical generation using templates.

Instead of generating ideas by reasoning about the problem domain, the code uses a small grammar:

- pick a "make" verb
- pick a noun with a matching article
- pick a transitive verb
- pick another noun with an article
- combine them into a phrase

The effect is intentionally offbeat and humorous, which matches the dojo challenge vibe. It is a simple example of how random vocabulary and fixed sentence patterns can produce a large number of semi-coherent prompts without needing a real AI model.

## The output

When run, the script emits a series of generated prompts, such as:

```text
Dojo, today you must construct an one that jolts an investment
Dojo, today you must arrange a leather that gathers a gold
Dojo, today you must cook a mark that wipes a quarter
```

The script loops 20 times and prints a different result every run.

This is the user-facing output: a stream of nonsense-but-structured challenge ideas, ready for a group to turn into actual project tasks.

## Summary

This project is a creative idea generator for the dojo. It combines random word lists and a fixed template to produce quirky task prompts that sound vaguely meaningful but are intentionally absurd. The code demonstrates a very lightweight form of procedural generation and is a good example of generating project ideas from word banks rather than from a database or external service.

It is not a serious problem-solving engine, but it is a fun, effective way to create fresh and chaotic brainstorming prompts for group sessions.
