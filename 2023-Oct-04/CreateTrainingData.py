import random
from pathlib import Path

if __name__ != "__main__":
  print("Running this file as a module is not supported")
  exit(1)


def control_function(celcius: float) -> float:
  """Correct conversion for testing"""
  return (celcius * 9 / 5) + 32


def create_traing_data() -> None:
  file_content = ""
  for _ in range(10000):
    x = random.randint(-100, 100)
    file_content += f"{x},{control_function(x)}\n"
  Path("training.txt").write_text(file_content)

create_traing_data()
