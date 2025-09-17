
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

from bs4 import BeautifulSoup
import requests
import sqlite3
import re

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
    def __init__(self, db_file:str):
        self.db_file = db_file
        self._create_db()

    def _create_db(self):
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
                """
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
    
    def get_all_clues(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            res = cursor.execute(
                """
                SELECT * FROM crossword ORDER BY id
                """
            )
            return res.fetchall() # Changed from `conn.fetchall` to `res.fetchall`

type HtmlPage = str
type JsonData = str

# Only does about 6 for now
_URL = "https://www.theguardian.com/crosswords"
def get_guardian_home_page() -> HtmlPage:
    """
    Gets the crossword home page
    """
    # Read this
    # https://www.geeksforgeeks.org/python/implementing-web-scraping-python-beautiful-soup/
    # then fill in:
    return requests.get(_URL).text

_HREF_REGEX = re.compile("/crosswords/[A-Za-z]+/[0-9]+")
def get_crossword_page(home_page:str) -> HtmlPage:
    """
    Gets a crossword page from a home page
    """
    # bs4 magic to get all hrefs with /crosswords/ inside
    print("<a" in home_page)
    soup = BeautifulSoup(home_page, 'html.parser')
    links = soup.find_all('a', href=_HREF_REGEX)

    for link in links:
        if link_text:= link.get("href"):
            # Prize crosswords don't have solutions so skip them
            if "prize" in link_text: continue
            # make absolute links
            yield requests.get(f"https://www.theguardian.com/{link_text}").text

def get_crossword_from_page(page:HtmlPage) -> JsonData:
    """
    Gets the json data from a crossword page
    """
    soup = BeautifulSoup(page, "html.parser")
    return soup.find("gu-island", attrs={"name":"CrosswordComponent"}).get("props")

def create_clue_from_data(id:int, clue_data:dict[str]):
    # solution needs some work:
    #   "separatorLocations" is a key:str value:list[int] pair 
    #   where key is the seperator (one of -,|)
    #   and value is where the seperator is
    #   so FLINTKNAPPING with {'-': [5]} becomes: FLINT-KNAPPING
    if "solution" not in clue_data.keys():
        print(clue_data)
    return Clue(id, clue_data["number"], clue_data["clue"], clue_data["solution"], clue_data["direction"] == "across")

def parse_crossword_data(json_crossword:JsonData) -> list[Clue]:
    """
    Turns a json string into a list of dataclasses
    """
    import json
    clue_dict = json.loads(json_crossword)["data"]
    id = clue_dict["number"]
    clue_data_list = clue_dict["entries"]
    return [ create_clue_from_data(id, clue_data) for clue_data in clue_data_list]
    
if __name__ == "__main__":
    def main():
        db = DataBase("all.db")
        home_page = get_guardian_home_page()
        for crossword_page in get_crossword_page(home_page):
            crossword:JsonData = get_crossword_from_page(crossword_page)
            open("out.json", "w").write(crossword)
            clues:list[Clue] = parse_crossword_data(crossword)
            for clue in clues: db.add_clue(clue)
        print(db.get_all_clues())
    main()

