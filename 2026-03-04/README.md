# Task

Generate a simple image by writing RGB pixel data in the plain-text PPM (Portable Pixmap) format.

## What the program does

The script in `Group-1/main.py` creates a 100-by-100 pixel image. `generate_pixels()` calculates an RGB colour for each coordinate: red increases with the x position, green increases with the y position, and blue decreases based on the smaller of those coordinates.

`convert_pixels_to_ppm()` writes a PPM header containing the image dimensions and maximum colour value, then formats each pixel as three decimal RGB values. `save_ppm()` saves the result as `go.ppm`. Running `main.py` regenerates that image file.

## Main concept

PPM is a simple image format that can represent an image as a header followed by raw pixel colour values. The code creates a P3 (plain-text) PPM, so each pixel is written as readable red, green, and blue integers in the range from 0 to 255.

This makes the relationship between program logic and image output direct: calculate a colour for every pixel, serialize the values in row-compatible image data, and save the text file with the PPM extension.

## Output

The output is `Group-1/go.ppm`, a 100-by-100 gradient image. It can be opened by image viewers that support the PPM format. The existing `go.ppm` is an example of the generated output.

## Summary

This project is a small image-generation experiment using the PPM format. It demonstrates how to produce a visual gradient from calculated RGB values without an image-processing library, by writing a plain-text image file directly.
