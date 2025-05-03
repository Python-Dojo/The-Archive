import random
# Hello I am Ray
# Blank to screen
# random 

# hola mi lla
# ma es Jorge

import os
import time as ModuleTime
from math import cos, sin

def iterate_code_rain_image(prev_image):
    row_length = len(prev_image[0])
    next_row =[[random.randint(0, 1) for _ in range(row_length)]]
    return next_row + prev_image[:-1]

def get_image(row_count, col_count):
    return [[random.randint(0, 1) for x in range(col_count)] for y in range(row_count)]
 

def get_image_circle(centre_x, centre_y, img_height, img_width, radius):
    img = [[0 for _ in range(img_width)] for _ in range(img_height)]
    
    for i in range(img_height):
        for j in range(img_width):
            if  0.5 < (i - centre_y)**2 + (j - centre_x)**2 / radius**2 < 1.4:
                img[i][j] = 1
    return img
    

frandom_str = ['~', 'Q', 'Q', 'Q', '2', 'U', ':', 'Q', 'Q', 'o', 'M', 'W', 'E', 'C', 'r', 'I', 'I', 'm', '^', '7', 'N', 'D', 's', 'Q', '0', 'j', 'B', 'L', 'Y', 'n', '@', 'J', 'i', 'z', '2', '3', 'y', 't', '<', 'Z', 't', 'M', '7', 's', 'T', 'q', 'B', 'Q', 'R', 'm', 'S', 'y', '6', 's', 'b', 'X', '5', '0', 'H', 'v', 'V', 'n', '?', 'q', 'x', 'S', 'I', 'W', 'C', 'F', 'A', 'N', 'P', '\\', 'O', 'k', 'L', '6', 'O', '=', 'm', 'c', '<', '6', '8', 'C', 'I', '8', 'E', 'I', '[', '2', 'V', 'X', 'Z', '6', 'J', '|', '7', 'e']

# Hello it is Will
class Scrolling():
    ASCII_START = 97
    ASCII_END = 122
    WIDTH = 100

    def __init__(self, img):
       self.img = img
        
    def add_rand_string(self):
        self.img = [(chr(random.randint(self.ASCII_START, self.ASCII_END))) for i in range (self.WIDTH)]


def display_binary_image(img):
    """
    img: [0 ,0, 0, 0, 0, 0, 0, 0,0]
         [0 ,0, 0, 1, 1, 1, 0, 0,0],
         [0 ,0, 1, 0, 1, 1, 1, 0,0],
         [0 ,0, 1, 0, 0, 0, 1, 0,0],
         [0 ,0, 0, 1, 1, 1, 0, 1,0],
         [0 ,0, 0, 0, 0, 0, 0, 0,0]
]      
    ]
    """
    for row in img:
        print("|", end="")
        for pixel in row:
            if pixel == 0:
                print(" ", end = "")
            elif pixel == 1:
                print("0", end="")
        print("|")
    print("-", end="")
    for column in img[0]:
        print("-", end="")
    print("-")


def main():
    termin_size = os.get_terminal_size()
    image = get_image(termin_size.lines - 2 , int(termin_size.columns - 3))
    for time in range(0, 100):
       os.system('clear') # cls on windows
       print()
       a = type(image)
       image = iterate_code_rain_image(image)
       assert type(image) == a
       display = display_binary_image(image)
       ModuleTime.sleep(1)

        

if __name__ == "__main__":
    main()