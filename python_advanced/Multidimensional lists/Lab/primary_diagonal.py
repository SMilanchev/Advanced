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


def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    size = len(matrix)
    for i in range(size):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


# def get_secondary_diagonal_sum(matrix):
#     diagonal_sum = 0
#     size = len(matrix)
#     for i in range(size):
#         diagonal_sum += matrix[i][size-i-1]
#     return diagonal_sum


print(get_primary_diagonal_sum(read_matrix()))