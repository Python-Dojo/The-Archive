from __future__ import annotations
from typing import Any
"""
Get percentage of lines written per user on a repo with the github api
"""
import logging
import requests
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

OWNER = "Python-Dojo"
REPO  = "The-Archive"

@dataclass
class Author:
    name: str
    additions: int
    deletions: int
    commits: int

    @classmethod
    def sum_commits(cls, weeks: list[dict[str, int]], key: str) -> int:
        return sum(week[key] for week in weeks)

    @classmethod
    def from_commit(cls, commit: dict[str, Any]) -> Author:
        author = commit["author"]
        weeks = commit["weeks"]
        return Author(
            name = author["login"],
            additions = cls.sum_commits(weeks, "a"),
            deletions = cls.sum_commits(weeks, "d"),
            commits = cls.sum_commits(weeks, "c")
        )
        

def get_authors(owner: str, repo: str) -> list[Author]:
    commits_raw = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stats/contributors")
    logging.info(commits_raw.status_code)
    if commits_raw.status_code > 299 or commits_raw.status_code < 200:
        raise Exception(f"bad request, code {commits_raw.status_code}")
    authors = [Author.from_commit(commit) for commit in commits_raw.json()] 
    return authors

def get_total_lines(authors: list[Author]) -> int:
    return sum(author.additions - author.deletions for author in authors)

def get_percentage_lines(author:Author, total:int):
    if total == 0:
        raise ValueError("No lines of code in repository")
    if total < 0:
        raise ValueError("What is this witchcraft")
    return (author.additions - author.deletions) / total * 100


if __name__ == "__main__":
    authors = get_authors(OWNER, REPO)
    total = get_total_lines(authors)
    for author in authors:
        lines = get_percentage_lines(author, total)
        print(f"{author.name} committed {lines:.2f}% of lines")
