def read_numbers():
    return list(map(int, input().split(', ')))


def num_list_to_str(nums):
    return ', '.join(map(str, nums))


numbers_list = read_numbers()
positive_nums = [x for x in numbers_list if x >= 0]
negative_nums = [x for x in numbers_list if x < 0]
even_nums = [x for x in numbers_list if x % 2 == 0]
odd_nums = [x for x in numbers_list if x % 2 != 0]

print(f'Positive: {num_list_to_str(positive_nums)}')
print(f'Negative: {num_list_to_str(negative_nums)}')
print(f'Even: {num_list_to_str(even_nums)}')
print(f'Odd: {num_list_to_str(odd_nums)}')
