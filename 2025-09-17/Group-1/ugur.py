"""
Scraping guardian crosswords with bs4
   - read the docs(?)
   - 
adding them to a sqlite database
 
 https://beautiful-soup-4.readthedocs.io/en/latest/
"""
import bs4
import requests
import sqlite3

db_file = "./crosswords"

# Get website by request
# def request_the_website():

# Parse the content by bs4

# Write by sqlite3 to db
def create_db(db_file):
    with sqlite3.connect(db_file) as conn:
        connect = conn.cursor()
        connect.execute(
            """
            CREATE TABLE crossword (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INT,
                clue TEXT,
                solution TEXT,
                down BOOL
            );
            """
        )
        conn.commit()

def add_crosswords(crossword_id, number, clue, solution, down):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO crossword (id, number, clue, solution, down)
            VALUES (?, ?, ?, ?, ?)
            """
            (crossword_id, number, clue, solution, down)
        )
"""
CREATE TABLE crossword (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clue TEXT,
    solution TEXT,
    direction BOOL
);
"""

