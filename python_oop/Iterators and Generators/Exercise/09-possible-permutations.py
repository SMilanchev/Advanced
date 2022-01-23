from itertools import permutations

def possible_permutations(nums: list):
    for el in permutations(nums):
        yield list(el)


print(next(possible_permutations([1, 2, 3])))
print(next(possible_permutations([1, 2, 3])))
print(next(possible_permutations([1, 2, 3])))
print(next(possible_permutations([1, 2, 3])))
print(next(possible_permutations([1, 2, 3])))
print(next(possible_permutations([1, 2, 3])))