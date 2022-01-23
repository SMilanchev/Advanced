def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    (rows_count, column_count) = map(int, input().split(', '))
    matirx = []
    for r in range(rows_count):
        row = list(map(int, input().split(' ')))
        matirx.append(row)
    return matirx


def get_column_sums(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    sums = []
    for column in range(columns_count):
        sums.append(0)
        for row in range(rows_count):
            sums[-1] += matrix[row][column]

    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix()
result = get_column_sums(matrix)
print_result(result)