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

    def __init__(self, *, control: bool, name: str) -> None:
        self._control = control
        self._name = name

    def __call__(self, function: Callable[P, T]) -> Callable[P, T]:
        """Add all the experimental only functions to the experiments list"""
        if not self._control:
            Experiment._experiments[self._name].append(function)
            Experiment._results[self._name][function.__name__] = ExperimentResult(matches=0, failures=0)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            """When we call the real function, run the experiments too"""
            real_result = function(*args, **kwargs)

            for experimental_function in Experiment._experiments[self._name]:
                experimental_result = experimental_function(*args, **kwargs)
                if experimental_result == real_result:
                    Experiment._results[self._name][experimental_function.__name__]["matches"] += 1
                else:
                    Experiment._results[self._name][experimental_function.__name__]["failures"] += 1

            return real_result
        return wrapper

@Experiment(control=True, name="experiment-1")
def legit_function(a: int, b: int, c: int) -> int:
    return sum([a, b, c])

@Experiment(control=False, name="experiment-1")
def bad_refactor(a: int, b: int, c: int) -> int:
    return a + b - c

@Experiment(control=False, name="experiment-1")
def good_refactor(a: int, b: int, c: int) -> int:
    return a + b + c

print(legit_function(1, 2, 3))
print(json.dumps(Experiment._results, indent=4))
