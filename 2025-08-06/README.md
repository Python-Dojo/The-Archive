# Task

Explore a custom voting system that selects a winner from ranked ballots, with the goal of reducing ties and giving support across a candidate's ranking history more weight than a simple vote total.

## What the program does

The main implementation is in `Group-2/main.py`. A `Poll` stores a list of candidate names and the ranks assigned to each candidate by submitted ballots. `add_ranking()` records each option's position in a ranking, and `pretty_print()` displays the collected rank data.

The script offers two scoring approaches:

- `get_scores_by_count()` counts how often each option appears at each rank.
- `get_weighted_scores()` sums the reciprocal of each rank, so first-place rankings contribute more than lower-ranked ones.

The active `winner()` method uses the weighted score and returns the candidate with the highest total. The example creates a poll, adds several rankings, prints the ballots, and prints the winning candidate.

`Group-1/main.py` explores a different design based on local contests by county. It counts votes for representatives and selects one for each county using a random choice weighted by vote count. It also sketches turning Discord reactions into votes. This is a separate prototype and does not implement the same ranked-ballot scoring system.

## Main concept

The central idea is to turn ranked ballots into scores, rather than considering only the top choice. In the Group 2 implementation, a candidate's score is the sum of `1 / rank` across submitted ballots. This is a simple positional scoring rule: candidates ranked highly by more voters tend to score better.

The Group 1 prototype instead uses weighted random selection among candidates within a county. That approach gives candidates with more votes a higher chance of selection, but it does not guarantee proportional representation.

## Output and limitations

Running `Group-2/main.py` prints the recorded rankings followed by the candidate with the highest reciprocal-rank score. The result is a single winner, not a distribution of seats or a complete proportional-representation result.

The single-transferable-vote method is only a placeholder. The implementation also permits duplicate candidates in a ranking, and ties are resolved by Python's `max()` behavior rather than an explicit tie-breaking rule. The Group 1 prototype has its own unfinished parts and does not provide a complete election workflow.

## Summary

This session experiments with ranked voting and alternative ways to select representatives. The most complete script calculates a reciprocal-rank score and prints one winner; another prototype explores county-level, vote-weighted random selection. The archived work demonstrates the scoring ideas, but does not yet deliver a full proportional voting system or a complete tie-resolution strategy.
