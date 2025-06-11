"""
What we are trying to achieve

def foo():
    return 1

@patch(foo, return_value=2)
def bar():
    assert foo() == 2

# bar should be ok
"""
from functools import wraps
import importlib


def patch(target, return_value):
    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            target_name = target.split(".")[-1]

            old_globals = old_function.__globals__
            initial = old_globals[target_name]
            old_globals[target_name] = lambda *args, **kwargs: return_value
            
            # run function whilst patched
            result = old_function(*args, **kwargs)

            old_globals[target_name] = initial

            return result
        return new_function
    return decorator
