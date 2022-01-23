def read_matrix():
    return [[int(x) for x in input().split(', ')] for _ in range(int(input()))]


def num_list_to_str(nums):
    return ', '.join(map(str, nums))


matrix = read_matrix()
size = len(matrix)

primary = [matrix[r][r] for r in range(size)]
secondary = [matrix[r][size - r - 1] for r in range(size)]

print(f'First diagonal: {num_list_to_str(primary)}. Sum: {sum(primary)}')
print(f'Second diagonal: {num_list_to_str(secondary)}. Sum: {sum(secondary)}')