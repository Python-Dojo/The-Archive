"""
The earth isn't flat but maps are... They use the markator projection to represent the earth on a 2d plane. 
This little game is inspired by the likes of "the true size of" and makes you guess which country is bigger. Given 2 countries and their rough size on a flat map, guess which is actually bigger."""

import random
import math


def game():
  """main game function promting the user with questions and answers."""
  countries = list(COUNTRY_AREA.keys())
  # country_a, country_b = random.choices(countries, k=2)
  country_a = random.choice(countries)
  countries.remove(country_a)
  country_b = random.choice(countries)
  size_a = calculate_area(country_a)
  size_b = calculate_area(country_b)
  # use f-string minilanguage to format your string
  # * `,` coma to separate thousands
  # * `..0f` to show 0 decimals
  print(
      f"Is {country_a} (map area: {size_a:,.0f}) larger than {country_b} (map area: {size_b:,.0f})?"
  )
  answer = (input("(Enter Yes/No):").lower().strip())
  if answer == "yes" and size_a > size_b:
    info = f"""Correct
    {country_a} (true area: {COUNTRY_AREA[country_a]:,.0f}) is larger than
    {country_b} (true area: {COUNTRY_AREA[country_b]:,.0f})
    """
    print(info)
    return True
  else:
    info = f"""Incorrect
    {country_a} (true area: {COUNTRY_AREA[country_a]:,.0f}) is smaller than
    {country_b} (true area: {COUNTRY_AREA[country_b]:,.0f})
    """
    print(info)
    return False


def calculate_area(country: str) -> float:
  latitude = LATITUDE_DEG[country]
  area = COUNTRY_AREA[country]
  return get_map_scaled_area(latitude, area)


LATITUDE_DEG = {
    "ENGLAND": 51.51,
    "WALES": 51.48,
    "GREENLAND": 64.17,
    "FRANCE": 48.86,
    "ICELAND": 64.15,
    "CONGO": 4.30,
}
COUNTRY_AREA = {
    "ENGLAND": 130279,
    "WALES": 21218,
    "GREENLAND": 2116000,
    "FRANCE": 551695,
    "ICELAND": 103000,
    "CONGO": 2345000
}


def get_mercator_scaling_factor(latitude_deg: float) -> float:
  rad = math.pi * latitude_deg / 180
  return math.cos(rad)


def get_map_scaled_area(latitude_deg: float, country_size: float) -> float:
  scaling_factor = get_mercator_scaling_factor(latitude_deg)
  rescaled_area = scaling_factor * country_size
  return rescaled_area


if __name__ == "__main__":
  while True:
    game()
