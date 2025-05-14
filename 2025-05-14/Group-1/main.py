import os
import time
import typing
from typing import Callable
import timeit

def profile_ours[R, **P](function:Callable[P, R]) -> Callable[P, R]:
    def _inner_profile(*args:P.args,**kwargs:P.kwargs) -> R:
        start = time.time_ns()
        function(*args, *kwargs)
        end = time.time_ns()
        time_ = end - start
        print(f"When called with arguments: {args=} {kwargs=} took {time_}ns")
    return _inner_profile 

def profile_timeit[R, **P](function:Callable[P, R]) -> Callable[P, R]:
    def _inner_profile(*args:P.args,**kwargs:P.kwargs) -> R:
        # timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
        f = function
        t = timeit.Timer(lambda: f(*args, *kwargs) , globals=globals())
        a = t.timeit(number=1) 
        print(f"When called with arguments: {args=} {kwargs=} took {int(a*(10**9))}ns")
    return _inner_profile

# testing

@profile_timeit
def foo0(some_value:int) -> None:
    for i in range(some_value):
        time.sleep(i/1000)


@profile_ours
def foo1(some_value:int) -> None:
    for i in range(some_value):
        time.sleep(i/1000)


if __name__ == "__main__":
    foo1(10)
    foo1(5)
    foo0(10)
    foo0(5)

    print("done")

def b(key:str):

    

    return { "a" : 1 , "b" : 2}.get(key)

MAP: dict[str, int] = { "a" : 1 , "b" : 2}



MAP.get("a")


"""
@decorator1
@decorator2
@time_ours
def bar1():
    # does stuff
    pass
"""