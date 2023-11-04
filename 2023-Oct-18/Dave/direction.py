from enum import Enum, EnumMeta
from point import Point


class DirectValueMeta(EnumMeta):
    # This allows us to unpack enum members directly, in the format:
    # row, col = Direction.RIGHT
    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value

    # This allows us to iterate through enum members in a for loop and access
    # the Point value directly
    def __iter__(cls):
        for value in super().__iter__():
            yield value.value


class Direction(Enum, metaclass=DirectValueMeta):
    RIGHT = Point(0, 1)
    DOWN = Point(1, 0)
    UP = Point(-1, 0)
    LEFT = Point(0, -1)
    UP_LEFT = Point(-1, -1)
    UP_RIGHT = Point(-1, 1)
    DOWN_LEFT = Point(1, -1)
    DOWN_RIGHT = Point(1, 1)
