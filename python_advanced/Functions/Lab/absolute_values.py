def convert_iterable_to_absolute(nums_list):
    return list(map(abs, nums))


nums = map(float, input().split(' '))
result = convert_iterable_to_absolute(nums)
print(result)