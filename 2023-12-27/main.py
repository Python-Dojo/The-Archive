import math
from typing import Tuple, Union
# log m^n=nlog(m)
anyNumber = Union[int,float]

# x^a * x^b => x^(a+b)
# (x^a)^b => x^(a*b)


def pow_any_square(number:int, exp:int) -> list[int]:
  ...

def pow_any_square(number:float, exp:int) -> list[float]:
  ...
# calculate pow for a square
def pow_any_square(number:anyNumber, exp:int) -> list[anyNumber]: # exp must be square number
  acc = number
  memoised = []
  memoised.append(number)
  max_iterations = int(math.sqrt(exp))
  for _ in range(max_iterations):
    acc *= acc
    memoised.append(acc)
  return memoised

# find highest square in number
def largest_square(number:anyNumber) -> Tuple[int, int]: 
  squares = [1,4,9,16,25,36,49,64,81,100]
  last_square = 1 
  for i, square in enumerate(squares):
    if square > number :
      return (i, last_square)
    last_square = square
  # TODO make this work
  return (10,100)

def pow_even(number, exp:int):
  index, largest_sqr = largest_square(exp)
  # x^2, x^4, 
  # x ^ ?
  memoised_pows = pow_any_square(number, largest_sqr)
  
  index, _ = largest_square(number - largest_sqr)
  memoised_pows[index] 


def pow(number, exp: int):
  # if odd -> (do for previous even) * number
  if (exp % 2 != 0):
    return pow(number, exp - 1) * number
  # if square -> keep squaring the 
  if (math.sqrt(exp) % 1 == 0):
    print("A")

  ...  # implent


def other_pow(number, exp):  #
  acc = number
  for _ in range(exp):
    acc *= number
  return acc


# A function a split up higher cases x^(>4)
if __name__ == "__main__":
  print(pow_any_square(2, 4), " should be 16")
  print(pow_any_square(2, 9), " should be ??")
