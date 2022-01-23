from collections import deque


def find_pureness(nums_list):
    sum = 0
    for n, v in enumerate(nums_list):
        sum += n * v

    return sum


def do_rotation(numbers):
    num = numbers.pop()
    numbers.appendleft(num)


def best_list_pureness(*args):
    numbers = deque(args[0])
    rotation_times = args[1]
    rotations = []
    for i in range(rotation_times + 1):
        current_pureness = find_pureness(numbers)
        rotations.append(current_pureness)
        do_rotation(numbers)

    max_pureness = max(rotations)
    index_max_pureness = rotations.index(max_pureness)
    return f'Best pureness {max_pureness} after {index_max_pureness} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
