# Task

Calculate how long remains until the next [Duck Thursday](https://www.youtube.com/watch?v=ZwCqnq9I1-A) a scheduled day defined by a configurable rule or list of dates.

## What the program does

The script in `Group-1/main.py` provides helpers to get the current time, calculate days until Thursday, find the next configured Duck Thursday, and convert the result into seconds. `Duck_Thursday_Config` is intended to accept either a predicate that identifies Duck Thursdays or an explicit list of dates.

When run directly, the script prints the current time-related values and exercises the date-finding helper with several sample configurations.

## Main concept

The program treats a recurring event as a date-selection problem:

1. Determine the current date and weekday.
2. Find a future date that matches the Duck Thursday rule.
3. Calculate the duration between now and that date.

The default rule uses Python's weekday numbering to locate Thursday. A custom predicate or list of dates is meant to allow other schedules without changing the search logic.

## Output and limitations

The intended output is the next Duck Thursday date and the number of seconds until it. The implementation is an experiment and has inconsistencies: the default helper returns a number of days despite its `datetime` return annotation, the list-based search uses repeated calls to the current clock, and `seconds_to_next_duck_thursday()` uses `timedelta.seconds`, which discards whole days. The configuration's date-list path also does not establish a stable reference time.

Consequently, the printed values are useful as a sketch of the countdown idea, but the code should not be relied on for an accurate event timer without corrections.

## Summary

This project explores a configurable countdown to a recurring special day. It combines weekday arithmetic, date predicates, and time deltas, with a small command-line demonstration. The intended result is a date and seconds-remaining display; the archived implementation still needs refinement to handle dates and durations consistently.
