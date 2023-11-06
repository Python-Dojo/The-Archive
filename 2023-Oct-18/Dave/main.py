import random
from copy import deepcopy
from word_grid import WordGrid
from point import Point
from direction import Direction
from placement import Placement
from exceptions import (
    FailedToGenerateWordSearchError,
    FailedToPlaceAllWordsError,
    NoLegalPlacementsError,
    GridOverflowError,
)


def main():
    word_list = ["PYTHON", "DOJO", "CODEHUB", "BRISTOL"]

    try:
        word_search = generate_word_search(rows=6, cols=9, word_list=word_list)
        print(word_search)
        print("Find these words:")
        print(", ".join(word_list))
    except FailedToGenerateWordSearchError:
        print("Failed to generate word search.")
        exit(1)


def generate_word_search(rows: int, cols: int, word_list: list[str]) -> WordGrid | None:
    word_grid = WordGrid(rows, cols)

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        word_grid.initialise_grid()
        try:
            filled_word_search = place_words(word_grid, word_list)
            filled_word_search.fill_blank_space()
            return filled_word_search
        except FailedToPlaceAllWordsError:
            attempts += 1
    else:
        raise FailedToGenerateWordSearchError()


def place_words(word_grid: WordGrid, word_list: list[str]) -> WordGrid:
    word_search = deepcopy(word_grid)

    for word in word_list:
        try:
            placements = get_all_legal_placements_for_word(word_search, word)
            position, direction = random.choice(placements)
            word_search.write_line(position, direction, word)
        except NoLegalPlacementsError:
            raise FailedToPlaceAllWordsError()

    return word_search


def get_all_legal_placements_for_word(
    word_grid: WordGrid, word: str
) -> list[Placement]:
    legal_placements = []

    # Iterate through all possible grid locations and orientations
    for row_index, row in enumerate(word_grid.grid):
        for col_index, col in enumerate(row):
            for direction in Direction:
                position = Point(row_index, col_index)

                line_can_be_written = word_grid.is_valid_line(
                    position, direction, len(word)
                )
                if not line_can_be_written:
                    continue

                target_line = word_grid.read_line(
                    position, direction, len(word))
                line_can_be_placed = is_legal_placement(
                    target_line=target_line, line_to_write=word
                )
                if not line_can_be_placed:
                    continue

                legal_placements.append(Placement(position, direction))

    if len(legal_placements) == 0:
        raise NoLegalPlacementsError()
    else:
        return legal_placements


def is_legal_placement(target_line: str, line_to_write: str) -> bool:
    for target_char, char_to_write in zip(target_line, line_to_write):
        if (char_to_write is not target_char) and (target_char != " "):
            return False
    return True


if __name__ == "__main__":
    main()
