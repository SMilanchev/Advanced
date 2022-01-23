def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(result):
    for el in result:
        print(el)


first, second = map(int, input().split(' '))
lines = input_to_list(first + second)

first_set = set(lines[:first])
second_set = set(lines[first:])

result = first_set.intersection(second_set)
print_result(result)

