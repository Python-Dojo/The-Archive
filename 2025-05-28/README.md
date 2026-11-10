# Task

Create a Git pre-commit hook that checks staged changes for a forbidden code pattern and blocks the commit when the pattern is found.

The prototype in `Group-1/main.py` searches for the regular expression `^import itertools`. Its intended behavior is to print an error and exit with status 1 when a matching added line is found, or print `good` and exit with status 0 otherwise.

## What the program does

The script defines `get_diff()` to retrieve staged Git changes and `do_regex()` to inspect lines, skipping removed lines and checking the remaining text against a compiled regular expression. `main()` uses those helpers to report whether the pattern is present.

The accompanying notes in `Group-1/README.md` describe installing the script as an executable hook in `.git/hooks` under the name `pre-commit`. Git runs that hook before completing a commit; a non-zero exit status is intended to reject the commit.

## Main concept

The main idea is to automate a lightweight lint check at commit time:

1. Read the staged diff.
2. Ignore removed lines so existing code being deleted does not trigger the rule.
3. Check added lines against a regular expression.
4. Return a failing status when a match is found.

This keeps the check focused on the changes being committed rather than scanning the entire repository.

## Output and current limitation

The intended output is either `bad` on standard error with exit status 1, or `good` with exit status 0.

As currently written, `get_diff()` requests Git's `--raw` output. Raw diff output describes file changes rather than including the added source lines, so `do_regex()` cannot reliably inspect staged code as intended. The script is therefore a prototype of a pre-commit check, not a working pattern scanner without adjusting how it retrieves the diff.

## Summary

This project explores using a Git pre-commit hook to enforce a simple regular-expression rule on staged code. It demonstrates the intended hook workflow and basic diff filtering, while the current diff format prevents the implementation from seeing the source lines it needs to check.
