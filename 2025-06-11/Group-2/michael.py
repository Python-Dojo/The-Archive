# 1.  Here are some nice inner functions
def inner_1(x):
    print(f"Run inner_1: {x}")
    return 1

def inner_2(x):
    print(f"Run inner_2: {x}")
    return 2

# 2. here are some nice alternative inner functions
def mock_inner_1(x):
    print(f"MOCK inner_1: {x}")
    return 101

def mock_inner_2(x):
    print(f"MOCK inner_2: {x}")
    return 102


# 3. here is an outer function
def outer():
    # we want to replace inner_X() -> mock_inner_X()
    inner_1(10)
    inner_2(10)


# 4. this takes 
def decorator_definer(inner_fun_name: str, mocked_inner_funname: str):

    def replace_inner_fun(old_outer_fun):

        def new_outer_fun(*args, **kwargs):
            """ This is a new copy of outer fucniotn that uses mocked internals """
            old_inner_fun = globals()[inner_fun_name]
            globals()[inner_fun_name] = globals()[mocked_inner_funname]
            result = old_outer_fun(*args, **kwargs)
            globals()[inner_fun_name] = old_inner_fun
            return result

        return new_outer_fun

    return replace_inner_fun

outer()

decorator_1 = decorator_definer("inner_1", "mock_inner_1")
decorator_2 = decorator_definer("inner_2", "mock_inner_2")

outer = decorator_1(decorator_2(outer))

outer()


def call_modified_outer(
    outer_func,
    mapping: dict[str, str],
):
    """ Call the outer funciotn after repalcing all the inners with mocked inners """
    pass


call_modified_outer(outer_func=outer, mapping = {"inner_1": "mocked_inner_1", "inner_2": "mocked_inner_2"})