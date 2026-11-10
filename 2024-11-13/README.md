# Task

Create a terminal-based animated code rain effect that fills the screen with flowing random characters.

This folder contains two different attempts from the 2024-11-13 Bristol Python Dojo session. Both are built around the same visual idea: simulate a classic "matrix-style" falling character stream in the terminal, with random characters drifting downward and refreshing like a rain animation.

## What the program does

### Group 1: animated binary rain

The script in `Group-1/main.py` builds a 2D grid of random values and repeatedly updates it to create a moving rain effect. The core logic is:

```python
def iterate_code_rain_image(prev_image):
    row_length = len(prev_image[0])
    next_row = [[random.randint(0, 1) for _ in range(row_length)]]
    return next_row + prev_image[:-1]
```

This moves the grid downward by shifting existing rows upward and adding a fresh top row. The result is a pseudo-random pattern that looks like falling code or flickering binary noise.

The script also includes helper functions to:

- generate a random image grid
- draw a simple binary image to the terminal
- display a visual pattern in a terminal-friendly format

It uses `os.get_terminal_size()` to adapt to the current window size and runs the animation in a loop with `os.system('clear')` and `time.sleep(1)`, producing a live screen refresh.

### Group 2: vertical falling character stream

The script in `Group-2/main.py` takes a slightly more object-oriented approach. It defines a `VertLine` class, where each falling column is a vertical stream with:

```python
class VertLine:
    def __init__(self):
        self.y = 0
        self.x = random.randint(0, screen_width - 2)
        self.c = random.choice(list("{}!\"£$%^&*()<>,./;'#:@~"))
```

Each line updates by moving downward:

```python
def update(self):
    self.y += 1
```

And the animation loop periodically creates new columns and renders them using the `curses` library:

```python
screen.addstr(line.y, line.x, line.c, 1)
```

This creates a more classic "digital rain" look, with individual columns of random symbols cascading down the terminal.

## Main concept

The central idea in both implementations is the same: create an illusion of motion by repeatedly redrawing a grid or stream of characters.

The effect works because each refresh cycle:

- moves the old pattern downward or shifts rows
- adds new random content at the top or in new columns
- clears the screen and re-renders the result

This makes the screen look alive, as if code is falling or dripping down the terminal.

The use of terminal APIs (`os.system('clear')`, `curses`) is key: it allows the program to animate directly inside the shell without needing a GUI.

## Output

The expected output is a live animated stream of random characters, ideally resembling a matrix-style terminal screen. In Group 1 it reads as binary-style noise; in Group 2 it is more like a stream of random punctuation and symbols falling down the screen.

The session is effectively building a visual effect generator, not a game or an app with a user model. The user-facing result is simply the animation itself.

## Summary

This session is a simple creative coding exercise in terminal animation. It explores how to use screen updates, random character generation, and coordinate-based movement to produce a falling-code aesthetic.

Both groups demonstrate the same principle in different ways:

- Group 1: grid-based shifting image
- Group 2: column-based falling characters using `curses`

The folders are rough prototypes, but they clearly capture the goal: build a terminal animation that looks like a digital rain effect from a sci-fi interface.
