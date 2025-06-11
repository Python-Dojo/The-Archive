# example of a decorator that prints out how long a function takes, and gets a bit creative :) 
import time

def define_decorator_definer(another_message):
    def define_decorator(special_message):
        def decorator(old_function):
            def new_function(*args, **kwargs):
                start_time = time.time()
                result = old_function(*args, **kwargs)
                end_time = time.time()
                print(another_message)
                print(special_message)
                print(f"function took {end_time - start_time}")
                return result
            return new_function
        return decorator
    return define_decorator


@define_decorator_definer("another message")("my random message")
def expensive():
    time.sleep(1)


expensive()