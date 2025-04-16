
from grid import Grid
import random 
import time

import os

def decide_fate(bias:float = 0.1):
    # bias is probability that a tile is alive
    random_fate = random.random()
    if random_fate < bias:
        return True
    else:
        return False
    # return random.choice((True, False))

def init_grid(bias:float = 0.5):
    grid = Grid()
    for row in grid.get_grid():
        for i in range(len(row)):
            row[i] = decide_fate(bias)
    return grid

def make_next_frame(previous_frame:Grid):
    next_frame = Grid()
    for row_index in range(Grid.GRID_SIZE):
        for column_index in range(Grid.GRID_SIZE):
            num_neighbours = previous_frame.count_neighbours(row_index, column_index)
            is_alive = previous_frame.get_grid()[row_index][column_index]
            if (is_alive):
                if not(num_neighbours < 2 or num_neighbours > 3):
                    next_frame.set_alive(row_index, column_index)
                    continue
            elif num_neighbours == 3:
                next_frame.set_alive(row_index, column_index)
    return next_frame

# ignore!
def alabhya_make_next_frame(previous_frame: Grid):
    for row in previous_frame:
        for col, elem in enumerate(row):
            is_alive = elem
            neighbors = previous_frame.count_neighbours(row, col)
            if neighbors < 2:
                elem = False
            if neighbors > 3:
                elem = False
            if not is_alive and neighbors == 3:
                elem = True

if __name__ == "__main__":
    base = init_grid()
    base.get_grid()[0][0] = True
    base.get_grid()[1][1] = True
    base.get_grid()[0][1] = True
    base.get_grid()[1][0] = True

    base.print()
    print()
    frame2 = make_next_frame(base)
    frame2.print()
    frames = 1000
    CLEAR_CMD = "clear"
    os.system(CLEAR_CMD)
    SLEEP_DURATION = 0.5
    time.sleep(SLEEP_DURATION)

    for i in range(frames):
        time.sleep(SLEEP_DURATION)
        base = make_next_frame(base)
        os.system(CLEAR_CMD)
        print(f"Itteration: {i}")
        
        base.print()



    print("hello world")
