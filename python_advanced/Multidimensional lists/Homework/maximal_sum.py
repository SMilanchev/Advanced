def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8,],
            [4, 8, 12, 16, 4],
        ]
    rows, columns = map(int, input().split())
    matirx = []
    for r in range(rows):
        row = list(map(int, input().split(' ')))
        matirx.append(row)
    return matirx


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            sum += matrix[r][c]

    return sum


def get_best_submatrix(matrix, submatrix_size):
    best_sum = 0
    best_row = 0
    best_col = 0
    for r in range(len(matrix) - submatrix_size + 1):
        for c in range(len(matrix[r]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, r, c, submatrix_size)
            if current_sum > best_sum:
                best_sum = current_sum
                best_col = c
                best_row = r

    return (best_row, best_col, best_sum)


def print_result(cooridantes, matrix_size):
    row, col, best_sum = cooridantes
    print(f'Sum = {best_sum}')
    for r in range(row, row + matrix_size):
        line = []
        for c in range(col, col + matrix_size):
            line.append(matrix[r][c])
        print(' '.join(str(x) for x in line))


SUBMATRIX_SIZE = 3
matrix = read_matrix(is_test=False)
print_result(get_best_submatrix(matrix, SUBMATRIX_SIZE), SUBMATRIX_SIZE)