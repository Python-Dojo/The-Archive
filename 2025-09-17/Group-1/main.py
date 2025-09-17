
# Scraping 
# guardian crosswords with bs4 
# Get website content
# Get a page with a crossword inside
# Get crossword data
# Parse crossword data (json)
# Format into dataclass
#
# SQLite
# go from dataclass into a column
# adding them to a sqlite database
# id per crossword
# isAcross bool
# clue number 
# clue string
# answer string

# https://beautiful-soup-4.readthedocs.io/en/latest/

import bs4
import requests

from dataclasses import dataclass

print("hello world")



@dataclass
class Clue:
    crossword_id: int
    number: int
    clue: str
    solution: str
    down: bool


dummy_clues = [
    Clue(1, 1, "hello ?????", "world", False),
    Clue(1, 2, "life, the universe and everything", "fortytwo", True),
    Clue(1, 3, "not yes", "no", False),
]


class MockDatabase:
    def __init__(self):
        self.clues = []

    def add_clue(self, clue: Clue):
        self.clues.append(clue)

    def get_all_clues(self):
        return self.clues
