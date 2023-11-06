import random
from word_grid import WordGrid
from point import Point
from direction import Direction
from placement import Placement


def main():
    word_list = ["MEOW", "CAT", "WOOF", "DOG"]

    word_search = generate_word_search(
        rows=4, cols=4, word_list=word_list)

    if word_search:
        print(word_search)
        print("Find these words:")
        print(", ".join(word_list))
    else:
        print("Failed to generate word search.")


def generate_word_search(rows: int, cols: int, word_list: list[str]) -> WordGrid | None:
    word_search = WordGrid(rows, cols)

    attempts = 0

    while attempts < 10:
        word_search.initialise_word_grid()
        filled_word_search = place_words(
            word_search=word_search, word_list=word_list)
        if filled_word_search:
            filled_word_search.fill_blank_space()
            return filled_word_search
        else:
            attempts += 1
            continue
    else:
        return None


def place_words(word_search: WordGrid, word_list=list[str]) -> WordGrid | None:
    filled_word_search = word_search

    for word in word_list:
        placements = get_all_legal_placements_for_word(
            word_grid=filled_word_search, word=word
        )
        if placements:
            position, direction = random.choice(placements)
            filled_word_search.write_line(
                position=position, orientation=direction, data=word
            )
        else:
            return None

    return filled_word_search


def get_all_legal_placements_for_word(
    word_grid: WordGrid, word: str
) -> list[Placement] | None:
    legal_placements = []

    # Iterate through all possible grid locations and orientations
    for row_index, row in enumerate(word_grid.grid):
        for col_index, col in enumerate(row):
            for direction in Direction:
                position = Point(row_index, col_index)

                target_line = word_grid.read_line(
                    position, direction, len(word))
                if not target_line:
                    continue

                line_can_be_placed = is_legal_placement(
                    target_line=target_line, line_to_write=word
                )
                if not line_can_be_placed:
                    continue

                legal_placements.append(Placement(position, direction))

    return legal_placements


def is_legal_placement(target_line: str, line_to_write: str) -> bool:
    for target_char, char_to_write in zip(target_line, line_to_write):
        if (char_to_write is not target_char) and (target_char is not " "):
            return False
    return True


if __name__ == "__main__":
    main()
