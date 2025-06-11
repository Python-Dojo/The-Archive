# foo passes to bar

# def decorator(old_function):
#     def new_function(*args, **kwargs):
#         result = old_function(*args, **kwargs)
#         return result
#     return new_function

def foo():
    return 1

def patch(target, return_value):
    def decorator(old_function):
        return old_function
    return decorator

@patch(foo, 2)
def bar():
    if foo() == 2:
        print("success")
    else:
        print("fail")

bar()
print(globals()["bar"])