from abc import ABC, abstractmethod


class Pattern(ABC):

  def match(self, input) -> bool:
    for i in self.matchStart(input):
      if i == []:
        return True
    return False

  @abstractmethod
  def matchStart(self, input):
    """
    Returns a generator that will find all matches, returning the 
    remaining input each time.
    """
    ...

  def concatenate(self, P):
    return Concatenate(self, P)

  def alternate(self, P):
    return Alternate(self, P)

  def repeat(self):
    return Repeat(self)

  def repeat1(self):
    # A+     A AA AAA AAAA
    # (A+)+  A AA AAA AAAA
    if isinstance(self, Repeat1):
      return self
    return Repeat1(self)

  def optional(self):
    """Equivalent to R?"""
    return Optional(self)


class Optional(Pattern):

  def __init__(self, original):
    self._original = original

  def matchStart(self, input):
    # Either we consume some input.
    for r in self._original.matchStart(input):
      yield r
    # Or we don't.
    yield input


class Concatenate(Pattern):

  def __init__(self, lhs, rhs):
    self._lhs = lhs
    self._rhs = rhs

  def matchStart(self, input):
    # _lhs and _rhs are predicates

    for remainsAfterLHS in self._lhs.matchStart(input):
      for remainsAfterRHS in self._rhs.matchStart(remainsAfterLHS):
        yield remainsAfterRHS


class Alternate(Pattern):
  """
  Equivalent to R|S 
  Matches against R or matches against S
  E.g. a|b   that will match 1 character which is either 'a' or 'b'
       abc|d that will match 3 characters (abc) or 1 character (d)
  """

  def __init__(self, lhs, rhs):
    self._lhs = lhs
    self._rhs = rhs

  def matchStart(self, input):
    for remainsAfterLHS in self._lhs.matchStart(input):
      yield remainsAfterLHS
    for remainsAfterRHS in self._rhs.matchStart(input):
      yield remainsAfterRHS


# Predicate is any function that given an input returns a bool.
class Predicate(Pattern):
"""Predicate is any function that given an input returns a bool."""

  def __init__(self, predicateFunction):
    self._pf = predicateFunction

  def matchStart(self, input):
    if input:
      if self._pf(input[0]):
        yield input[1:]


class Repeat(Pattern):

  def __init__(self, original):
    self._original = original

  def matchStart(self, input):
    # Zero iteration of original pattern.
    yield input
    for r in self._original.matchStart(input):
      # Recursively iterate more.
      yield from self.matchStart(r)


# Match one or more times.
class Repeat1(Pattern):

  def __init__(self, original):
    self._original = original

  def matchStart(self, input):
    for r in self._original.matchStart(input):
      yield r
      # Recursively iterate more.
      yield from self.matchStart(r)


if __name__ == "__main__":

  # p1 = Predicate(lambda x: x == "abc")
  # p1.match(['abcabc', 'aabbcc', 'abcccc']) # False
  # p1.match(['abc'])                        # True
  # Would it not only match p1.match('abc')? .... 'abc' ... 'a', 'b', 'c'

  p1 = Predicate(lambda x: x == "abc")
  print(p1.match([]))
  print(p1.match(['abc']))
  print(p1.match(['abc', 'pqr']))
  print(p1.match(['abxc']))

  print("---")

  p2 = Concatenate(p1, p1)
  print(p2.match([]))
  print(p2.match(['abc']))
  print(p2.match(['abc', 'abc']))
  print(p2.match(['abc', 'abc', 'pqr']))

  print("---")

  p_int = Predicate(lambda x: isinstance(x, int))
  print(p_int.match([5]))
  print(p_int.match(["foo"]))
  print(p_int.match([5, 6]))

  print("---")

  p_one_or_two = p_int.concatenate(p_int).alternate(p_int)
  p_one_or_two = Alternate(Concatenate(p_int, p_int), p_int)
  for remainder in p_one_or_two.matchStart([5, 6, 7]):
    print(remainder)

  print("---")

  for remainder in p_int.repeat1().repeat1().matchStart([5, 6, 7, 'x']):
    print(remainder)
