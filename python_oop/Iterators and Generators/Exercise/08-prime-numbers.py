from typing import List


def get_primes(numbers: List[int]):
    for num in numbers:
        if is_prime(num):
            yield num


def is_prime(num: int):
    dividers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_divisible = lambda x: (x % m == 0 for m in dividers if m != x)
    if num <= 1 or any(is_divisible(num)):
        return False
    else:
        return True


for num in get_primes([2, 4, 3, 5, 6, 9, 1, 0]):
    print(num)