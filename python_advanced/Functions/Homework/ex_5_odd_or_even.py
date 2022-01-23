def is_odd(x):
    return x % 2 != 0


def is_even(x):
    return x % 2 == 0


command = input()
nums_list = list(map(int, input().split(' ')))
numbers_length = len(nums_list)

if command == 'Odd':
    odd_nums = filter(is_odd, nums_list)
    print(sum(odd_nums)*numbers_length)
elif command == 'Even':
    even_nums = filter(is_even, nums_list)
    print(sum(even_nums)*numbers_length)
