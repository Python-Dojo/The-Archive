
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
import sqlite3

from dataclasses import dataclass

@dataclass
class Clue:
    crossword_id: int
    number: int
    clue: str
    solution: str
    down: bool

    def __hash__(self):
        return hash((self.crossword_id, self.number, self.clue, self.solution, self.down))


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


class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_db()

    def create_db(self):
        with sqlite3.connect(self.db_file) as conn:
            connect = conn.cursor()
            connect.execute(
                """
                CREATE TABLE crossword (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    crossword_id INT,
                    number INT,
                    clue TEXT,
                    solution TEXT,
                    down BOOL
                );
                """
            )
            conn.commit()

    def add_crosswords(self, crossword_id, number, clue, solution, down):
        """Adds Crossword to the crossword db"""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"""
                INSERT INTO crossword (crossword_id, number, clue, solution, down)
                VALUES (?, ?, ?, ?, ?)
                """,
                (crossword_id, number, clue, solution, down)
            )
            conn.commit()

    def add_clue(self, clue: Clue):
        self.add_crosswords(
            clue.crossword_id, clue.number, clue.clue, clue.solution, clue.down
        )
    
    # def get_all_clues(self) -> list[Clue]:
    def get_all_clues(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            res = cursor.execute(
                """
                SELECT * FROM crossword ORDER BY id
                """
            )
            return res.fetchall() # Changed from `conn.fetchall` to `res.fetchall`
    
    # def get_the_clue(self, clue: Clue):
    #     with sqlite3.connect(self.db_file) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             """
    #             SELECT *
    #             """
    #         )

