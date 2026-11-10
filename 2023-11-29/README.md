# Task

Create a fraction calculator or arithmetic library that can handle rational numbers accurately, including decimal inputs and operations such as addition, subtraction, multiplication, division, and conversion to floating-point values.

This date folder contains three different attempts from the 2023-11-29 Bristol Python Dojo session. The shared idea is to represent numbers as fractions, avoid floating-point precision problems, and implement arithmetic operations in a mathematically clean way.

## The shared challenge

The main theme is that ordinary floating-point arithmetic can produce surprising results such as:

```python
0.1 + 0.2
```

which is not exactly `0.3` in binary floating-point. A fraction-based representation avoids that problem by storing values as numerator and denominator pairs.

Each group approaches this in a different way:

- Group 1 implements a Python `Fraction` class
- Group 2 sketches a parser for sums of fractions and decimals
- RayCPP.cpp builds a C++ fraction library with constexpr-style arithmetic and numeric concepts

## Group 1: Python fraction class

Directory: `Group-1`

File: `main.py`

This is the clearest and most direct implementation in the folder.

It defines a `Fraction` dataclass-like class with a custom constructor:

```python
@dataclass
class Fraction:
    def __init__(self, numerator, denominator=1):
        self.nominator = numerator
        self.denominator = denominator
```

It then implements arithmetic methods such as:

- `__add__`
- `__sub__`
- `__mul__`
- `__div__`

The arithmetic is standard rational arithmetic:

```python
nominator = (self.nominator * frac.denominator) + (frac.nominator * self.denominator)
denominator = self.denominator * frac.denominator
return Fraction(nominator, denominator)
```

It also includes methods to:

- convert the fraction to a float
- format the fraction as a string
- add support for decimal-to-fraction conversion by using `as_integer_ratio()`

The main demonstration includes examples such as:

```python
print(Fraction(2, 10) + (Fraction(4, 2)), "Should be 2.2")
print(Fraction(1) + Fraction(4), " Should be 5")
print(Fraction(5, 2) * Fraction(6, 1) - Fraction(6, 3), " Should be 13")
```

This makes it the simplest, easiest-to-follow fraction implementation in the archive and a good reference for the idea behind the whole session.

## Group 2: parsing arithmetic expressions with fractions and decimals

Directory: `Group-2`

File: `main.py`

This is a more exploratory and incomplete attempt. It tries to parse user input such as:

```text
+Y+Z+...
```

and detect whether each value is:

- a fraction like `3/4`
- a decimal like `0.25`
- or something else

The code begins with a function named `input_determination()` that reads from input and splits a sum expression using `+`:

```python
of_values_in_sum=str(input('Input the sum of fractions and/or decimals you want to add in form +Y+Z+...')).split('+').strip()
```

It then tries to inspect each fragment:

- if it contains `/`, interpret it as a fraction
- if it contains `.`, interpret it as a decimal

The script also includes a helper `turn_to_int(num: float) -> Tuple[int, int]` that converts a decimal into a numerator and scale factor by examining the decimal point position.

This is a promising idea, but the implementation is incomplete and contains broken Python syntax and unfinished logic. It serves as an example of a parser design that never fully reached a working state.

## Ray C++: templated fraction arithmetic in C++

Directory: `RayCPP.cpp`

This is a C++ attempt to create a rational-number type with high-level arithmetic, constexpr support, and template constraints.

The file defines concepts such as:

```cpp
template<typename T>
concept AnyInt = std::is_integral<T>::value;

template<typename T>
concept AnyFloat = std::is_floating_point<T>::value;

template<typename T>
concept Number = (AnyFloat<T> || AnyInt<T>);
```

It then defines a `Fraction` class with constructors for:

- integer numerator/denominator pairs
- float-to-fraction conversion
- generic arithmetic operators

Important features include:

- overloaded arithmetic operators for `+`, `-`, `*`, `/`
- comparison support via `<=>`
- conversion between floating-point and fraction representations
- a `StringToFraction()` helper that parses strings such as `"1/2"` and `"3.1415"`
- user-defined literal support like `"1/2"_F` and `0.2_F`

This is the most ambitious version in the folder: it tries to make a fraction type that behaves elegantly in modern C++ and can convert decimal and string representations into exact rational values.

The file also includes test prints, for example:

```cpp
PrintFractionTest(Fraction(2, 10) + Fraction(4, 2), 2.2);
PrintFractionTest(0.2_F + 2_F, 2.2);
PrintFractionTest("1/2"_F + 1, 1.5);
```

This shows the intent clearly: build a strongly typed numeric class that preserves exact arithmetic while still working naturally with standard numeric values.

## Common techniques across the folder

All three attempts use similar conceptual ideas:

- carry numerator and denominator together
- reduce or keep exact values rather than approximating floating-point arithmetic
- support operations like addition and multiplication mathematically
- convert decimal values to fractions where needed
- use tests to validate expected outputs

The Python and C++ solutions all reflect the same principle: exact rational arithmetic can be more reliable than using binary floating-point numbers directly.

## Why this matters

This session is useful because it demonstrates how a seemingly simple problem — arithmetic with fractions — becomes surprisingly deep when you look at edge cases such as:

- decimal inputs
- mixed integer and fraction expressions
- precision and rounding
- string parsing
- operator overloading
- template-based numerics in C++

The code is not polished, but it is a clear record of the team's exploration of exact arithmetic.

## Running the examples

Python examples can be run from the relevant directories:

```bash
cd 2023-11-29/Group-1
python main.py
```

```bash
cd 2023-11-29/Group-2
python main.py
```

The C++ file is a standalone source file and would need to be compiled with a C++ compiler, for example:

```bash
g++ -std=c++20 RayCPP.cpp -o fraction_demo
./fraction_demo
```

## Summary

The 2023-11-29 session is a strong example of a dojo problem that can be approached in multiple programming languages and styles:

- Group 1: straightforward Python fraction class
- Group 2: unfinished parser for mixed arithmetic input
- RayCPP.cpp: ambitious C++ rational arithmetic with user-defined literals and concepts

Together, the folder shows a range of ways to think about exact numeric representation and arithmetic. The code is experimental and rough, but the ideas are sound and the session produced a useful progression of prototypes.
