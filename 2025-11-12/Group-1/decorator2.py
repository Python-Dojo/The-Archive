from typing import TypedDict
from collections import defaultdict
from collections.abc import Callable
import json

class ExperimentResult(TypedDict):
    matches: int
    failures: int

class Experiment[**P, T]:

    _experiments: dict[str, list[Callable]] = defaultdict(list)
    _results: dict[str, dict[str, ExperimentResult]] = defaultdict(dict)

    def __init__(self, *, control: str|Callable[P, T]) -> None:
        self._control = control if isinstance(control, str) else control.__name__

    def __call__(self, function: Callable[P, T]) -> Callable[P, T]:
        """Add all the experimental only functions to the experiments list"""
        if self._control == function.__name__:
            Experiment._experiments[self._control].append(function)
            Experiment._results[self._control][function.__name__] = ExperimentResult(matches=0, failures=0)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            """When we call the real function, run the experiments too"""
            real_result = function(*args, **kwargs)

            for experimental_function in Experiment._experiments[self._control]:
                experimental_result = experimental_function(*args, **kwargs)
                if experimental_result == real_result:
                    Experiment._results[self._control][experimental_function.__name__]["matches"] += 1
                else:
                    Experiment._results[self._control][experimental_function.__name__]["failures"] += 1

            return real_result
        return wrapper

class Raysperiment[**P, T]:
    def __init__(self, control:Callable[P, T]) -> None:
        self._functions = []
        self._control = control
        self._results: dict[str, ExperimentResult] = defaultdict(lambda:ExperimentResult(matches=0, failures=0))

    def register(self, function:Callable[P, T]) -> Callable[P, T]:
        self._functions.append(function)
        return function
    
    def handle_result(self, function_name: str, good: T, unknown: T) -> None:
        if good == unknown:
            self._results[function_name]["matches"] += 1
        else:
            self._results[function_name]["failures"] += 1

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        real_result = self._control(*args, **kwargs)
        for func in self._functions:
            unknown = func(*args, **kwargs)
            self.handle_result(func.__name__, real_result, unknown)
        return real_result

legit_function = Raysperiment(control=lambda a, b, c:sum([a, b, c]))

@legit_function.register
def bad_refactor(a: int, b: int, c: int) -> int:
    print("a + b - c")
    return a + b - c

@legit_function.register
def good_refactor(a: int, b: int, c: int) -> int:
    print("a + b + c")
    return a + b + c

print(legit_function(1, 2, 3))
print(json.dumps(legit_function._results, indent=2))
