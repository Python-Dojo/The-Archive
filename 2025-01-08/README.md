# Task

Measure how much code each contributor has written in the repository by querying GitHub’s contributor stats API.

This folder contains a Python script from the 2025-01-08 dojo session. The task is to compute the percentage of repository changes attributed to each author by reading GitHub contributor data and summing the additive and subtractive line changes across commit history.

## What the program does

The main script in `Group-1/main.py` defines an `Author` dataclass and a few functions to fetch and process contributor data from GitHub.

It does the following:

- calls `https://api.github.com/repos/{owner}/{repo}/stats/contributors`
- parses each contributor entry
- sums the total additions, deletions, and commit counts
- calculates the percentage of net lines each author contributed to the repository

The key code is:

```python
def get_authors(owner: str, repo: str) -> list[Author]:
    commits_raw = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stats/contributors")
    authors = [Author.from_commit(commit) for commit in commits_raw.json()]
    return authors
```

This is the core of the data collection step.

## Main concept

The main idea is surprisingly simple: use GitHub’s contributor stats as an estimate of contribution volume and compare authors by net lines changed.

The script computes:

```python
def get_total_lines(authors: list[Author]) -> int:
    return sum(author.additions - author.deletions for author in authors)
```

Then for each author it calculates:

```python
def get_percentage_lines(author: Author, total: int):
    return (author.additions - author.deletions) / total * 100
```

This gives a rough percentage breakdown of repository changes by contributor, based on the delta in line counts rather than a stricter metric such as commit count or review participation.

## Output

When run, the program prints a result like:

```text
<author> committed 12.34% of lines
```

This is a useful summary for understanding who has contributed most to the repository by line count.

## Summary

This project is a lightweight repository contribution analysis tool. It fetches GitHub contributor statistics and turns them into a readable summary of author activity. It is a very practical coding challenge because it combines API access, data parsing, and simple statistics in one focused script.

The implementation is intentionally compact and readable, and the real value is in turning raw GitHub contributor information into a useful output that can tell you who has added or removed the most lines in a project.
