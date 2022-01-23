from typing import Callable
import pprint


def cache(func: Callable) -> Callable:
    log = {}

    def wrapper(args):
        if args not in log:
            res = func(args)
            log[args] = res
            return res
        return log[args]

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(100)
pprint.pprint(fibonacci.log)