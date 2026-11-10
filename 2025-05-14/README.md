# Task

Compare ways to measure how long a Python function takes to run by implementing timing decorators.

The code in `Group-1/main.py` defines two decorators, `profile_ours` and `profile_timeit`, and applies them to sample functions. The examples call functions that sleep for a small amount of time, making the elapsed duration easy to observe.

## What the program does

`profile_ours` records a start and end time using `time.time_ns()`, calculates the elapsed nanoseconds, and prints the function arguments and duration.

`profile_timeit` uses Python's `timeit.Timer` to measure a call and prints the elapsed time converted to nanoseconds. The script runs both decorated examples with different inputs and then prints `done`.

## Main concept

A decorator wraps a function so that extra behavior can happen when the function is called. Here, the wrapper is intended to time the call without changing the decorated function's call site:

```python
@profile_ours
def foo1(some_value: int) -> None:
    ...
```

The session compares a direct clock-based measurement with the standard library's `timeit` utility. It also explores preserving callable argument and return types with generic type parameters.

## Output

Running the script is intended to print timing messages for each sample call, including the arguments and elapsed nanoseconds, followed by `done`.

The decorators are unfinished: they call the wrapped function with `*kwargs` instead of `**kwargs`, and they do not return its result. The sample functions only use positional arguments, so the invocation issue is not exposed by the included calls. The measured times are illustrative; the examples include `sleep`, so they primarily measure the requested delay rather than the speed of useful computation.

## Summary

This folder contains a small experiment in function timing and decorators. It demonstrates two approaches to measuring elapsed time and how wrappers can add instrumentation around function calls. The intended output is a per-call duration report, though the prototypes need fixes before they support keyword arguments or preserve return values.
