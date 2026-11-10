# Task

Organise dojo participants into balanced teams using their experience ratings and admin status.

The ratings are represented as numbers from 0 to 10, with `11` reserved for an admin. The goal is to make teams that are similar in size and overall experience, while ensuring each team has an admin where possible.

## What the programs do

The two groups contain separate attempts at the team-assignment problem.

`Group-1/main.py` starts with validation and group-count logic. It counts admins, rejects invalid ratings, and begins assigning admins to groups. The implementation ends unfinished, so it does not yet distribute all participants or produce final teams. `Group-1/test.py` exercises some of the group-count and admin-assignment behavior.

`Group-2/main.py` takes a more complete greedy approach. It calculates a number of teams intended to keep team sizes within a maximum of six, sorts participants from highest rating to lowest, and repeatedly assigns the next person to the team with the lowest current rating total. It prints the sorted ratings and the resulting team totals and participant identifiers.

## Main concept

The main concept is balancing teams using a greedy load-distribution algorithm:

1. Determine how many teams to create from the number of participants.
2. Sort participants by rating.
3. Assign each participant to the team with the smallest current total.
4. Report each team's total rating and membership.

The first attempt also treats admins specially and defines a minimum team size. The second focuses on keeping accumulated rating totals close. Together they explore different constraints involved in team assignment: team size, rating balance, and admin coverage.

## Output

The Group 2 script prints a JSON-formatted list of team rating totals and a corresponding list of participant identifiers for each team. Its sample input is generated at runtime, so the exact participants and totals vary between runs.

The output is a draft team allocation, not a fully validated schedule: the code does not enforce all of the documented requirements, such as guaranteeing one admin per team or keeping every team within both the stated minimum and maximum sizes.

## Summary

This session explores how to distribute participants into reasonably even teams based on experience scores, while accounting for admin availability. Group 1 sketches validation and admin placement; Group 2 implements a simple greedy balancing strategy and prints the resulting buckets. Both are prototypes, and neither fully solves every constraint described in the task.
