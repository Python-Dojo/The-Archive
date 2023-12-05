# R := N
# Q := 0
# while R ≥ D do
#   R := R − D
#   Q := Q + 1
# end
# return (Q,R)


def division(numerator, denominator):
  remainder = numerator
  quotient = 0
  while remainder >= denominator:
    remainder = remainder - denominator
    quotient = quotient + 1
  return (quotient, remainder)


def format_as_decimal(fraction, precision):
  numerator, denominator = map(int, fraction.split("/"))
  digits, _ = division(numerator * 10**precision, denominator)
  return f"0.{digits}"
