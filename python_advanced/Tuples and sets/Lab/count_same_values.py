values = map(float, input().split())

values_dict = {}

for value in values:
    if value not in values_dict:
        values_dict[value] = 0
    values_dict[value] += 1

for (num, count) in values_dict.items():
    print(f'{num} - {count} times')