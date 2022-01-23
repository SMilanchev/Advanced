def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())

# lines = [
#     '0,3-1,2',
#     '2,10-3,5',
#     '6,15-3,10',
# ]

lines = input_to_list(n)
longest_intersection = ""
for line in lines:
    (range_1, range_2) = line.split('-')
    set_one = set()
    set_two = set()
    intersection = set()
    for num in range(int(range_1.split(',')[0]), int(range_1.split(',')[1])+1):
        set_one.add(num)
    for num in range(int(range_2.split(',')[0]), int(range_2.split(',')[1]) + 1):
        set_two.add(num)
    intersection = set_one.intersection(set_two)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')