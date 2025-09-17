

import requests

# TODO: import
@dataclass
class Clue:
    crossword_id: int
    number: int
    clue: str
    solution: str
    down: bool


type HtmlPage = str
type JsonData = str


_URL = "https://www.theguardian.com/crosswords"
def get_guardian_home_page() -> HtmlPage:
    """
    Gets the crossword home page
    """
    # Read this
    # https://www.geeksforgeeks.org/python/implementing-web-scraping-python-beautiful-soup/
    # then fill in:
    return requests.get(_URL)


def get_crossword_page(home_page:str) -> HtmlPage:
    """
    Gets a crossword page from a home page
    """
    ...

def get_crossword_from_page(page:HtmlPage) -> JsonData:
    """
    Gets the json data from a crossword page
    """
    ...

def parse_crossword_data(json_crossword:JsonData) -> list[Clue]:
    """
    Turns a json string into a list of dataclasses
    """
    ...

def is_crossword_page(link_address:str) -> bool:
    # href = /crosswords/{crossword_type}/{number}

if __main__ == "__main__":
    def main():
        home_page = get_guardian_home_page()
        for links in bs4.links(home_page):
            if 
