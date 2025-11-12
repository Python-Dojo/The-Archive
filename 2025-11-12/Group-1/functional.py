import typing


def run_experiment[T, **P](candidate: typing.Callable[P, T]) -> typing.Callable[P, T]:
    def inner(control: typing.Callable[P, T]) -> typing.Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            e = experiment(control, candidate, *args, **kwargs)
            return e

        return wrapper

    return inner


def sum_n_bad(n: int) -> float:
    return sum(i for i in range(1, int(n) + 1))


@run_experiment(sum_n_bad)
def sum_n_good(n: int) -> float:
    return n * (n + 1) / 2


def experiment[T, **P](
    control: typing.Callable[P, T],
    candidate: typing.Callable[P, T],
    *args: P.args,
    **kwargs: P.kwargs,
) -> T:
    control_result = control(*args, **kwargs)
    candidate_result = candidate(*args, **kwargs)
    if control_result == candidate_result:
        print("equivalent!")
    else:
        print("different!")

    return control_result


def experiment_with_comparison[T, **P](
    control: typing.Callable[P, T],
    candidate: typing.Callable[P, T],
    comparison: typing.Callable[[T, T], bool],
    *args: P.args,
    **kwargs: P.kwargs,
) -> T:
    control_result = control(*args, **kwargs)
    candidate_result = candidate(*args, **kwargs)
    if comparison(control_result, candidate_result):
        print("equivalent!")
    else:
        print("different!")

    return control_result


def experiment_with_comparison_and_enabled[T, **P](
    control: typing.Callable[P, T],
    candidate: typing.Callable[P, T],
    comparison: typing.Callable[[T, T], bool],
    enabled: typing.Callable[[], bool],
    *args: P.args,
    **kwargs: P.kwargs,
) -> T:
    control_result = control(*args, **kwargs)
    if enabled():
        candidate_result = candidate(*args, **kwargs)
        if comparison(control_result, candidate_result):
            print("equivalent!")
        else:
            print("different!")

    return control_result


if __name__ == "__main__":
    sum_n_good(10.0)
