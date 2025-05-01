from __future__ import annotations
"""
The plan

- Setup initial grid of some size/ get the size of the users window
- every x seconds, spawn a new bit of random code
- create class for vertical line of rain?

"""
import curses
import random


class VertLine:
    def __init__(self):
        self.y = 0
        self.x = random.randint(0, screen_width - 2)
        self.c = random.choice(list("{}!\"£$%^&*()<>,./;'#:@~"))

    def update(self):
        """moves down"""
        self.y += 1
        
    def is_valid(self):
        return self.y < screen_height

screen = curses.initscr()
screen_height, screen_width = screen.getmaxyx()
lines: list[VertLine] = []

while True:
    screen.clear()
    lines.append(VertLine())
    for line in lines:
        line.update()
        if line.is_valid():
            screen.addstr(line.y, line.x, line.c, 1)
    screen.refresh()
    curses.napms(300)
