def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    size = int(input())
    matirx = []
    for r in range(size):
        row = list(map(int, input().split(' ')))
        matirx.append(row)
    return matirx


def find_primary_diagonal(matrix):
    size = len(matrix)
    sum = 0
    for r in range(size):
        sum += matrix[r][r]
    return sum


def find_secondary_diagonal(matrix):
    size = len(matrix)
    sum = 0
    for r in range(size):
        sum += matrix[r][size - r - 1]
    return sum


matrix = read_matrix()
result = abs(find_primary_diagonal(matrix) - find_secondary_diagonal(matrix))
print(result)