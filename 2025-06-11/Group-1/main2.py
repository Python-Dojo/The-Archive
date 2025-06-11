# inspo: https://github.com/adamchainz/patchy

import inspect
import ast
from types import CodeType
from typing import Any, Callable
from contextlib import contextmanager


@contextmanager
def patch(target: Callable[..., Any], new_source: str):
    original_source = inspect.getsource(target)
    result: CodeType | ast.Module = compile(new_source, "<string>", "exec")
    target.__code__ = result
    target()
    yield

    result: CodeType | ast.Module = compile(original_source, "<string>", "exec")
    target.__code__ = result
    target()
    return


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(add(3, 3))

    with patch(add, "def add(a:int, b:int) -> int:\n\treturn a * b"):
        print(add(3, 3))

    print(add(3, 3))
