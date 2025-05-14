# Profiling with decorators

Make the following print out how long the function took:
```Python
@profile
def foo(some_value:int) -> None:
    for i in range(some_value):
        something()
```

Example decorators:
```Python
def outer(func:typing.Callable):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner
```