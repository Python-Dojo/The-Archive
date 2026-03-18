
"""
calculate the amount of seconds until the next duck thursday
"""

# TODO:
#   - get current time datetime.now
#   - configure next duck thursday
#   - duck thursday - now 
#   - arg parse

import datetime
import typing
import unittest


def get_current_time():
    ctime = datetime.datetime.now()
    return ctime

WEEKDAY_LOOKUP: dict[int, str] = { 0 : "Monday", 1 : "Tuesday", 2: "Wednesday", 3: "Thursday", 4 : "Friday", 5 : "Saturday", 6: "Sunday" }

class Duck_Thursday_Config:
    def __init__(self, option: typing.Callable | list[datetime.datetime]):
        self.pattern = option if isinstance(option, typing.Callable) else None
        self.duck_thursdays = option if isinstance(option, list) else None
        assert(self.pattern is not None or self.duck_thursdays is not None)
    
    def is_duck_thursday(self, to_check :datetime.datetime) :
        if self.pattern is not None:
            return self.pattern(to_check)

def get_days_until_next_duck_thurdsay(config: Duck_Thursday_Config | None = None) -> datetime.datetime :
    """Gets the next duck thursday (from today)"""
    if config is None:
        duck_thursday = 3
        weekday = get_current_time().weekday()
        # 3 - 1 => 2 Monday (2)     2  => 9      2 % 7 => 2
        # 3 - 4 => -1 Friday (6)    -1 => 6     -1 % 7 => 6
        return (duck_thursday - weekday) % 7
    current = get_current_time();
    if (config.pattern is not None):
        for _ in range(99999):
            current += datetime.timedelta(days=1)
            if config.is_duck_thursday(current):
                return current
        raise Exception("NO DUCk THURSDAY?!")
    if config.duck_thursdays is not None:
        for duck in config.duck_thursdays:
            if duck > get_current_time() + datetime.timedelta(days=1): # + 1 
                return duck
        raise Exception("NO DUCk THURSDAY?!")
    raise Exception("Config was not valid")


def time_until_midnight():
    midnight = datetime.datetime.combine(get_current_time().date(), datetime.time())
    return midnight

def time_at_start_of_day(the_day:datetime.datetime):
    midnight = datetime.datetime.combine(the_day.date(), datetime.time())
    return midnight

def get_next_duck_thursday() -> datetime.datetime:
    days_left = get_days_until_next_duck_thurdsay()
    # days left to duration
    days_left = datetime.timedelta(days=days_left)
    # add duration to now
    next_duck_thursday = days_left + datetime.datetime.now()
    # round to start of day
    next_duck_thursday = time_at_start_of_day(next_duck_thursday)
    # return that^
    return next_duck_thursday

def seconds_to_next_duck_thursday() -> int:
    duration = get_next_duck_thursday() - datetime.datetime.now()
    return duration.seconds

def assert_no_throws(callable, *args):
    try:
        callable(*args)
        return True
    except:
        return False

def assert_throws(callable, *args):
    try:
        callable(*args)
        return False
    except:
        return True

if __name__ == "__main__":
    print("Hello duck world")
    print(time_until_midnight())
    print(get_next_duck_thursday())
    print(seconds_to_next_duck_thursday())
    print(assert_throws(get_days_until_next_duck_thurdsay, Duck_Thursday_Config([]) ))
    print(assert_throws(get_days_until_next_duck_thurdsay, Duck_Thursday_Config( lambda a : False ) ))
    print(assert_no_throws(get_days_until_next_duck_thurdsay, Duck_Thursday_Config( lambda a : True ) ))
    print(get_days_until_next_duck_thurdsay( Duck_Thursday_Config( lambda a : a < datetime.datetime.now() + datetime.timedelta(days=1) ) ))


    
