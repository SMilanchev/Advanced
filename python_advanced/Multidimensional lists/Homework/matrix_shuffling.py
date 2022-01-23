def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
        ]
    rows, columns = map(int, input().split())
    matirx = []
    for r in range(rows):
        row = input().split(' ')
        matirx.append(row)
    return matirx


def is_command_valid(input_command, matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    row_1, col_1, row_2, col_2 = map(int, input_command[1:])
    if row_1 >= matrix_rows or col_1 >= matrix_columns or row_2 >= matrix_rows or col_2 >= matrix_columns:
        return False
    else:
        return True


def swapping_matrix_elements(matrix, indexes):
    row_1, col_1, row_2, col_2 = map(int, indexes)
    old_index = matrix[row_1][col_1]
    matrix[row_1][col_1] = matrix[row_2][col_2]
    matrix[row_2][col_2] = old_index

    return matrix


def print_current_matrix(matrix):
    for el in matrix:
        print(' '.join(map(str, el)))


matrix = read_matrix()
END_COMMAND = 'END'
while True:
    command = input()
    if command == END_COMMAND:
        break
    command = command.split(' ')
    if command[0] == 'swap':
        if is_command_valid(command, matrix):
            print_current_matrix(swapping_matrix_elements(matrix, command[1:]))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')