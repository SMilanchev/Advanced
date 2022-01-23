def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(result):
    for el in result:
        print(el)


elements_count = int(input())

# lines = [
#     'Ce O',
#     'Mo O Ce',
#     'Ee',
#     'Mo',
# ]
lines = input_to_list(elements_count)

elements_set = set()
for line in lines:
    elements = line.split()
    for element in elements:
        elements_set.add(element)

print_result(elements_set)