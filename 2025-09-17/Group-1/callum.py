
import bs4
import requests
from dataclasses import dataclass
import sqlite3

def get_guardian_site(id: int):
    guardian_url = "https://www.theguardian.com/crosswords/quick/"
    r = requests.get(guardian_url + str(id))
    print(r.status_code)


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

def test_database(database):
    # make some toy data
    ......

    # add to teh database
    for clue in dummy_clues:
        database.add_clue(clue)

    # load all cluses form the database
    retrieved_clues = database.get_all_clues()

    # loop over all clues, check the clues before and after are the same
    for clue


class DataBase:
    def __init__(self):
        self.clues = []

    def add_clue(self, clue: Clue):
        self.clues.append(clue)


if __name__ == "__main__":


    test_database()
