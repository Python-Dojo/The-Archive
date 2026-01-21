import random


def make_mine_grid(
    height: int = 11,
    width: int = 12,
    ratio: float = 0.1,
) -> list[list[int]]:
    """
    Make a grid of booleans for bomb locations.
    """
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for row_idx in range(height):
        for col_idx in range(width):
            if random.random() < ratio:
                grid[row_idx][col_idx] = 1

    return grid


def number_to_emoji(n: int) -> str:
    """Make it angrier red as the number increases \033[38;2;146;255;12m"""
    intensity = [255, 150, 110, 80, 60, 40, 30, 0]

    r, g, b = (255, intensity[n], intensity[n])
    return f"\033[38;2;{r};{g};{b};12m{n}"


def do_the_thing(input: list[list[bool]]) -> None:
    for y, row in enumerate(input):
        for x, v in enumerate(row):
            if v:
                print("💣", end="")
                continue

            adjacent_mines = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    yy = y + i
                    xx = x + j
                    if yy < 0 or xx < 0 or yy >= len(input) or xx >= len(row):
                        continue
                    if input[yy][xx]:
                        adjacent_mines += 1
            print(f"{number_to_emoji(adjacent_mines)}", end=" ")
        print()


if __name__ == "__main__":
    from pprint import pprint

    grid = make_mine_grid()

    pprint(grid)
    print("\n\n")

    do_the_thing(grid)
