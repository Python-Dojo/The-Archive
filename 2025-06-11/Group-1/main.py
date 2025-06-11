from contextlib import contextmanager
from typing import Any
import unittest.mock as mock

def add(a: int, b: int) -> int:
    return a + b

def greeter(name: str) -> None:
    print(f"Hello, {name}")

def python_stdlib_example():
    print(f"Not mocked: {add(3,4)}")

    with mock.patch("__main__.add") as mocked_add:
        mocked_add.return_value = -1
        print(f"Mocked: {add(3,4)}")
    
    print(f"Not mocked: {add(3,4)}")

def patch_with_mock_example():
    print(f"Not mocked: {add(3,4)}")
    def mult(a:int, b:int) -> int:
        return a*b
    mock_obj = mock.Mock(side_effect=mult)
    with patch_with_mock(f"__main__.add", mock_obj):
        print(f"Mocked: {add(3,4)}")
        
    print(f"Not mocked: {add(3,4)}")

def patch_example(function, *args):
    print(f"Not mocked: {function(*args)}")
    with patch_with_mock(f"__main__.{str(function)}", -1):
        print(f"Mocked: {function(*args)}")
        
    print(f"Not mocked: {function(*args)}")


#Assumption: focused on top level view of the function.
#Cyber risk management: patch function does not leave, callable, executable outside the test environment.

@contextmanager
def patch(function_name: str, return_value: Any):
    import importlib
    module_name, *attrs = function_name.split(".")
    assert len(attrs) == 1
    module = importlib.import_module(module_name)
    old = getattr(module, attrs[0])
    setattr(module, attrs[0], lambda *args, **kwargs: return_value)
    yield
    setattr(module, attrs[0], old)
    
@contextmanager
def patch_with_mock(function_name: str, called_mock: None | mock.MagicMock = None ):
    import importlib
    module_name, *attrs = function_name.split(".")
    assert len(attrs) == 1
    module = importlib.import_module(module_name)
    old = getattr(module, attrs[0])
    if called_mock is None:
        called_mock = mock.MagicMock()
    setattr(module, attrs[0], called_mock)
    yield
    setattr(module, attrs[0], old)
    


if __name__ == "__main__":
    print(add)
    print("=== Standard library ===")
    python_stdlib_example()

    print("=== Our version ===")
    # patch_example(add, 3, 4)
    patch_with_mock_example()
