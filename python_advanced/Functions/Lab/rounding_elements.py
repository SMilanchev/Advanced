def round_iterable_elements(nums_list):
    return list(map(round, nums_list))


nums = map(float, input().split(' '))
result = round_iterable_elements(nums)
print(result)