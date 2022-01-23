def find_ascii_sum(word):
    current_sum = 0
    for ch in line:
        current_sum += ord(ch)

    return current_sum


def is_number_even(number):
    return True if number % 2 == 0 else False


def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(even_set, odd_set):
    if sum(odd_set) == sum(even_set):
        result = odd_set.union(even_set)
    elif sum(odd_set) > sum(even_set):
        result = odd_set - even_set
    else:
        result = odd_set.symmetric_difference(even_set)

    print(", ".join(list(map(str, result))))


n = int(input())
lines = input_to_list(n)

set_even_nums = set()
set_odd_nums = set()

for i in range(len(lines)):
    line = lines[i]
    current_sum = int(find_ascii_sum(line)/(i+1))
    if is_number_even(current_sum):
        set_even_nums.add(current_sum)
    else:
        set_odd_nums.add(current_sum)

print_result(set_even_nums, set_odd_nums)