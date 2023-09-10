import random

CORRECT_AREA:float 


def parse_line(line:str) -> tuple[str, float]:
  i = 0  
  for char in line:
    if char.isdigit():
      break
    i += 1
  return (line[:i], float(line[i:].replace(",", "")))
    
print(parse_line(" hello 9,0"))


def find_in_file(place_name:str) -> tuple[str, float]|None:
  with open('map_big.txt') as f:
    i:int = 0
    for row in f.readline():
      if place_name in row:
        return parse_line(place_name)
      i += 1
    return None

def create_guess() -> tuple[str,float]:
  with open("map_big.txt") as file:
    lines = file.readlines()
    index = random.randrange(0, len(lines))
    return parse_line(lines[index])

def print_guess() -> None:
  global CORRECT_AREA
  conuntry, CORRECT_AREA = get_guess()
  print(f"guess the country with the closest area to {conuntry} ")
  

def get_guess() -> tuple[str, float]:
  while(True):
    guess:str = input("Please guess")
    a = find_in_file(guess)
    if a is None :
      print("That guess was not a valid conutry")
      continue
    return a


def compare_guesses(guess, correct) -> None:
  print(f"you guessed {guess[0]} which has a size of {guess[2]}")
  print(f"The country actually has an area of ")
  
  #basic validate guess (no numbers, code etc)  
  
  return guess;

#main
create_guess()

compare_guesses()
