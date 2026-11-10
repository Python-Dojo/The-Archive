# Task

Implement the numbers round from the television game *Countdown*: use up to six selected numbers and the basic arithmetic operations to reach a randomly chosen three-digit target.

## What the programs do

`Group-2/main.py` contains a recursive expression search. It selects six numbers from the standard pools—small numbers from 1 to 10 and large numbers 25, 50, 75, and 100—then generates a target from 100 to 999. The search repeatedly combines two available expressions using addition, subtraction, multiplication, or exact integer division. When only one expression remains, it checks whether that expression equals the target and prints matches.

`Group-1/main.py` explores a different, more heuristic strategy. It factors the target into primes, tries to match or combine those factors with the available numbers, and recursively attempts arithmetic constructions. It also includes random number and target generation, plus a few hand-picked success/failure examples. The search functions are unfinished and do not reliably find solutions.

`RayPy/main.py` is only a short import experiment referencing database classes; it does not implement a separate Countdown solver.

## Main concept

The central problem is a constrained search over arithmetic expressions. Each selected tile may be used at most once, operations must combine currently available values, and division must produce an integer. The recursive solver explores possible pairings and operation choices, carrying the expression along with each intermediate result so it can show how a solution was formed.

The prime-factor approach tries to reduce the target to factors that may be constructed from the input tiles. It is an alternative heuristic, but arithmetic solutions can involve subtraction and intermediate values that do not correspond neatly to the target's prime factors.

## Output

The Group 2 script prints the random target and selected numbers, followed by any exact expressions it finds. If no exact expression is found, the result list is empty; it does not report the closest reachable value.

The Group 1 script prints diagnostic information and attempts to print or validate candidate expressions in its example code, but its unfinished search logic means its output is not dependable.

## Summary

This session explores two ways to solve the Countdown numbers game: exhaustive recursive expression search and a prime-factor-based heuristic. The recursive version is the more complete prototype and aims to show exact arithmetic solutions using the chosen tiles. The work is experimental, and search efficiency, robust solution reporting, and nearest-result handling remain open improvements.
