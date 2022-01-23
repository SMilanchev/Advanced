def create_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(input())
        matrix.append(row)
    return matrix


def find_current_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "P":
                return r, c


def is_valid_position(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True


def print_result(matrix):
    [print("".join(row)) for row in matrix]


string = input()
n = int(input())
matrix = create_matrix(n)

commands = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

m = int(input())
for _ in range(m):
    command = input()
    current_row, current_col = find_current_position(matrix)
    new_x, new_y = current_row + commands[command][0], current_col + commands[command][1]
    if is_valid_position(matrix, new_x, new_y):
        symbol = matrix[new_x][new_y]
        matrix[current_row][current_col] = '-'
        if symbol.isalpha():
            string += symbol
        matrix[new_x][new_y] = 'P'
    else:
        if string:
            string = string[:-1]
        break


print(string)
print_result(matrix)