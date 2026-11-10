# Task

Build an experiment framework that compares a trusted implementation of a function with one or more candidate replacements, using the same inputs to check whether their outputs agree.

## What the programs do

The main prototype is in `Group-1/main.py`. A `BackwardCompatibleExperiment` stores a control function and candidate functions. Each call runs the control and candidates with the same arguments, compares their results, and records match and failure counts by candidate name.

`decorator.py` explores a decorator-based API: a control function is wrapped so that experimental implementations run alongside it, while the control result is still returned to the caller. `decorator2.py` experiments with registering candidate functions against a named control. `functional.py` presents a simpler function/decorator approach and adds optional custom comparison and enablement callbacks.

These are multiple sketches of the same idea rather than a single integrated package. Some examples execute when imported, and the designs vary in how candidates are registered and how results are stored.

## Main concept

The framework is intended for safely evaluating a refactor or replacement without changing the user-visible result. Production behavior continues to come from the established control function; candidate implementations are run in parallel for observation, and their outputs are compared and counted.

This is useful for shadow testing or gradual migrations: exercise a new implementation on real inputs, record where it agrees or diverges, and defer switching callers until confidence is high.

## Output

The examples print the control result and a summary of candidate matches and failures. The functional version prints whether the two results are equivalent. The expected output is therefore a small report that helps assess whether a candidate behaves like the trusted implementation.

The prototypes have rough edges. For example, the main class does not return the control result from `run()`, the decorator examples use shared class-level registries, and the implementations do not handle candidate exceptions or side effects. They demonstrate the concept, not a production-ready compatibility-testing framework.

## Summary

This session explores a way to compare old and new implementations under identical inputs while continuing to use the old implementation's result. The central output is agreement statistics that can guide a migration. The different files try context-managed, decorator-based, and functional APIs for registering and running candidate implementations.
