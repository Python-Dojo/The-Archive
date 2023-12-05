# Fractional calcuator

# https://stackoverflow.com/questions/29495169/how-to-create-the-divide-method-in-python

from dataclasses import dataclass


@dataclass
class Fraction:

    def __init__(self, numerator, denominator=1):
        self.nominator = numerator
        self.denominator = denominator

    def to_fraction(any_type):
        if (type(any_type) == float):
            nominator, denominator = any_type.as_integer_ratio()
            Fraction(nominator, denominator)
        if (type(any_type) == int):
            Fraction(any_type, 1)

    def __str__(self):
        return f"{str(self.nominator)}/{str(self.denominator)} ({self.as_float()}) "

    def as_float(self) -> float:
        return self.nominator / self.denominator

    def __add__(self, frac):
        nominator = (self.nominator * frac.denominator) + (frac.nominator *
                                                           self.denominator)
        denominator = self.denominator * frac.denominator
        return Fraction(nominator, denominator)

    def __sub__(self, right_hand_side):
        nominator = (self.nominator * right_hand_side.denominator) - (
            right_hand_side.nominator * self.denominator)
        denominator = self.denominator * right_hand_side.denominator
        return Fraction(nominator, denominator)

    def __mul__(self, frac):
        nominator = self.nominator * frac.nominator
        denominator = self.denominator * frac.denominator
        return Fraction(nominator, denominator)

    def __div__(self, rhs):
        nominator = self.nominator * rhs.denominator
        denominator = self.denominator * rhs.nominator
        return Fraction(nominator, denominator)


if __name__ == "__main__":
    print(Fraction(2, 10) + (Fraction(4, 2)), "Should be 2.2")
    print(Fraction(1) + Fraction(4), " Should be 5")
    print(Fraction(5, 2) * Fraction(6, 1) - Fraction(6, 3), " Should be 13")
    print(Fraction(1, 10) + Fraction(2, 10), " should be 0.3")
    print((0.1 + 0.2))
