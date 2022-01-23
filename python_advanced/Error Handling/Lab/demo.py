import time
from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(50))
end = time.time()
print(end-start)