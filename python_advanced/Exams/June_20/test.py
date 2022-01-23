def best_list_pureness(*args):
    return args[0]


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(test)

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
