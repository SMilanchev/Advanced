def read_matrix():
    rows = int(input())
    return [list(map(int, input().split(' '))) for _ in range(rows)]


def are_coordinates_valid(matrix, row, column):
    size = len(matrix)
    return 0 <= row < size and 0 <= column < size


def add_number(matrix, row, column, number):
    matrix[row][column] += number


def subtract_number(matrix, row, column, number):
    matrix[row][column] -= number


def print_result(matrix):
    [print(' '.join(str(x) for x in line)) for line in matrix]


matrix = read_matrix()
while True:
    command = input().split(' ')
    if command[0] == 'END':
        print_result(matrix)
        break
    row, column, num = map(int, command[1:])
    if are_coordinates_valid(matrix, row, column):
        if command[0] == 'Add':
            add_number(matrix, row, column, num)
        elif command[0] == 'Subtract':
            subtract_number(matrix, row, column, num)
    else:
        print('Invalid coordinates')
