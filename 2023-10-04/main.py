# machine learning

# create random list of eq to init

# loop
#   test and score all eq s
#   take top 10% and make children (similar eqs)

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import random

def load_training_terms() -> list[tuple[float, ...]]:
  data = Path("training.txt").read_text().split("\n")
  pairs = [
    tuple(map(float, line.split(","))) for line in data
  ]
  return pairs

@dataclass
class Term:

  def __init__(self, x2, x, c):
    self.x2 = x2
    self.x = x
    self.c = c

  def __str__(self):
    return f"{self.x2=},{self.x=},{self.c=}"

def foo() -> str:
  return ""

if __name__ == "__main__":
  print("this is main")


def create_random_term() -> Term:
  terms = [random.uniform(-10, 10) for _ in range(3)]
  return Term(*terms)


def init_terms(number:int = 100):
  terms = [
    create_random_term() for _ in range(number)
  ]
  return terms


def create_child(random_min_max: float, parent: Term) -> Term:
  x2 = parent.x2 + random.uniform(-random_min_max, random_min_max)
  x = parent.x + random.uniform(-random_min_max, random_min_max)
  c = parent.c + random.uniform(-random_min_max, random_min_max)
  return Term(x2, x, c)


def test_term(term: Term) -> tuple[float, float, float]:
  y_error:float = 0;
  for x, y_actual in  load_training_terms():
    try:
      y = term.x2**x + term.x*x + term.c;
    except:
      y = 10000000000000; 
    y_error += abs(y_actual - y);

  return y_error, y_error, y_error;

def main():
  terms = init_terms(100)
  errors:list[tuple[float, Term]] = []
  i = 1
  while True:
    print("testing ")
    for a in terms:
      error, _, _ = test_term(a)
      errors.append((error, a))
    print("sorting")
    errors.sort(key = lambda x: x[0]);
    print("culling")
    errors = errors[0:len(errors)//10];
    print("clearing")
    terms = [];
    for error, term in errors:
      for _ in range(10):
        terms.append(create_child(error/(100000/i), term))
    print("clearing")
    errors = [];
    print(terms[0])
    i += 1 
  
main()
