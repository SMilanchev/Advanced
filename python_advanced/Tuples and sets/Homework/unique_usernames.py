def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(result):
    for el in result:
        print(el)


# lines = [
#     'George',
#     'George',
#     'George',
#     'Peter',
#     'George',
#     'NiceGuy1234',
# ]

count = int(input())
lines = input_to_list(count)
print_result(set(lines))