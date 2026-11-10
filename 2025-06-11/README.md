# Task

Re-create the core idea behind Python's `unittest.mock.patch`: temporarily replace a function or other callable during a test, then restore the original afterward.

## What the programs do

The session contains several experiments in `Group-1` and `Group-2`.

`Group-1/main.py` implements context managers that replace a named attribute in a module, either with a constant-returning function or with a supplied mock. Its examples compare the replacement behavior with `unittest.mock.patch`.

`Group-1/main2.py` explores a more ambitious alternative: inspect a function's source, compile replacement source code, and swap the function's code object for the duration of a context manager.

The Group 2 scripts explore decorator-based patching. They temporarily replace a function in another function's globals, allowing a test function to run with a controlled dependency. Other files demonstrate a timing decorator and compare the experiments with the standard library's patching tools.

## Main concept

Patching provides test isolation by replacing a dependency only while a particular test or block runs. A typical lifecycle is:

1. Save the original callable.
2. Install a replacement or mock.
3. Run the code under test.
4. Restore the original callable.

The examples investigate different interfaces for this lifecycle: context managers, decorators, module attribute lookup, and direct function-code replacement.

## Output and limitations

The example scripts print results showing when the original or replacement function is called, and whether a test sees the mocked return value. The timing example prints its messages and elapsed duration.

These are experiments, not a finished replacement for `unittest.mock.patch`. The custom context managers do not use `try/finally`, so an exception inside the patched block can leave the replacement installed. The code-object approach is especially fragile because compiled source must match the target function's code expectations. For normal testing, Python's standard `unittest.mock.patch` remains the reliable option.

## Summary

This session explores how temporary function replacement can make tests more controlled and predictable. The code demonstrates several ways to patch dependencies and restore them afterward, while also showing why lifecycle safety and compatibility make a general-purpose mocking library more involved than a simple reassignment.
