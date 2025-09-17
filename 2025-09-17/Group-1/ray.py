

import requests
from bs4 import BeautifulSoup
import re
from dataclasses import dataclass

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
            # make absolute links
            yield requests.get(f"https://www.theguardian.com/{link_text}").text

def get_crossword_from_page(page:HtmlPage) -> JsonData:
    """
    Gets the json data from a crossword page
    """
    soup = BeautifulSoup(page, "html.parser")
    return soup.find("gu-island", name="CrosswordComponent").get("props")

def parse_crossword_data(json_crossword:JsonData) -> list[Clue]:
    """
    Turns a json string into a list of dataclasses
    """
    ...

if __name__ == "__main__":
    def main():
        home_page = get_guardian_home_page()
        for crossword_page in get_crossword_page(home_page):
            crossword:JsonData = get_crossword_from_page(crossword_page)
            clues:list[Clue] = parse_crossword_data(crossword)
            # add to database
    main()
                
