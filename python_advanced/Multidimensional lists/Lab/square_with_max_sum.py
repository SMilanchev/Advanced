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
        row = list(map(int, input().split(', ')))
        matirx.append(row)
    return matirx


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]

    return the_sum


def get_best_submatrix(matrix, submatrix_size):
    best_row = 0
    best_col = 0
    best_sum = get_sum_of_submatrix(matrix, best_row, best_row, submatrix_size)

    for row in range(len(matrix) - submatrix_size + 1):
        for c in range(len(matrix[row]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row, c, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row = row
                best_col = c

    return (best_row, best_col)


def print_result(coordinates, size):
    (rows, cols) = coordinates
    for r in range(rows, rows + size):
        line = []
        for c in range(cols, cols + size):
            line.append(matrix[r][c])
        print(' '.join(str(x) for x in line))
    print(get_sum_of_submatrix(matrix, rows, cols, size))


SUBMATRIX_TEST = 2

matrix = read_matrix()
coordinates = get_best_submatrix(matrix, SUBMATRIX_TEST)
print_result(coordinates, SUBMATRIX_TEST)

