from main import patch
import importlib

def foo():
    return 1


@patch("katie.foo", return_value=2)
def bar():
    print("im being called")
    if foo() == 2:
        print("success")
    else:
        print("fail")


if __name__ == "__main__":
    bar()