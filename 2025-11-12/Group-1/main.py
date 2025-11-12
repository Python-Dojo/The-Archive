"""
experiments framework 
    (i.e. take a function and an alternative implementation 
    and compare that their outputs are the same)
"""

"""
# ktl example
args = (1, 2)
kwargs = {"arg1": "string"}

experiment = Experiment("my-experiment")
experiment.control(control_func, args=args, kwargs=kwargs)
experiment.candidate(candidate_func, args=args, kwargs=kwargs)

result = experiment.conduct()
"""

# So do you end up replacing
# result = function(*args, **kwargs)
# with
# experiment.control(function, args=args, kwargs=kwargs)
# result = experiment.conduct()



# TODO:
#   Write a function that takes two inputs
#   Run the first function with inputs
#   Run second fucntion with the same inputs
#   Check outputs are the same
#   Log success/failure for inputs

# Possible impls:
#   - one function takes 2 inputs, register then call
#   - builder pattern that take 

from typing import Callable, TypedDict

class Result(TypedDict):
    matches: int
    failures: int


class BackwardCompatibleExperiment[**P, T]:

    def __init__(self):
        self._control_function:Callable[P, T] | None = None
        self._new_functions:set[Callable[P, T]] | None = None
        self._matches: dict[str, Result] = {}

    def register_functions(self, battle_tested: Callable[P, T], new_funcs: set[Callable[P, T]]) -> None:
        self._control_function = battle_tested
        self._new_functions = new_funcs

        for func in new_funcs:
            self._matches[func.__name__] = Result(matches=0, failures=0)

    def handle_result(self, function_name: str, good: T, unknown: T) -> None:
        if good == unknown:
            self._matches[function_name]["matches"] += 1
        else:
            self._matches[function_name]["failures"] += 1

    def run(self, *args: "P.args", **kwargs: "P.kwargs") -> T:
        known_result = self._control_function(*args, **kwargs)
        for func in self._new_functions:
            result = func(*args, **kwargs)
            self.handle_result(func.__name__, known_result, result)

import sys
def main():
    experimant = BackwardCompatibleExperiment();
    def foo(i:int):
        return int(i) - 1
    def bar(j:float):
        return j-1
    experimant.register_functions(foo, {bar})
    experimant.run(float(sys.maxsize))
    print(experimant._matches)


if __name__ == "__main__":
    main()

