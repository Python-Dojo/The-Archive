"""
Shaders!
using PPM format
to make a thing https://www.shadertoy.com/view/NddGzH
https://en.wikipedia.org/wiki/Netpbm

e.g.
"""

SAMPLE_PPM = """P3
3 2
255
255   0   0
  0 255   0
  0   0 255
255 255   0
255 255 255
  0   0   0
"""

MAX_X = 100
MAX_Y = 100
SF = 255 / MAX_X


def generate_pixels() -> list[tuple[int, int, int]]:
    pixels = []
    for x in range(MAX_X):
        for y in range(MAX_Y):
            pixels.append((int(x * SF), int(y * SF), int(255 - min(x, y) * SF)))
    return pixels


def convert_pixels_to_ppm(pixels: list[tuple[int, int, int]]) -> str:
    header = f"P3\n{MAX_X} {MAX_Y} \n255"
    lines = [f"{r:>3} {g:>3} {b:>3}" for r, g, b in pixels]
    content = "\n".join(lines)
    return f"{header}\n{content}\n"


def save_ppm(ppm: str) -> None:
    with open("go.ppm", "w") as t:
        t.write(ppm)


def main() -> None:
    pixels = generate_pixels()
    ppm = convert_pixels_to_ppm(pixels)
    save_ppm(ppm)


if __name__ == "__main__":
    main()
