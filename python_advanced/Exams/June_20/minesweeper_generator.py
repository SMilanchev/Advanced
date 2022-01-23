def create_matrix(size):
    matrix = []
    for _ in range(size):
        row = [0 for i in range(size)]
        matrix.append(row)
    return matrix


def is_valid_coordinate(matrix, current_x, current_y, add_x, add_y):
    size = len(matrix) - 1
    new_x = current_x + add_x
    new_y = current_y + add_y
    if 0 <= new_x <= size and 0 <= new_y <= size and matrix[new_x][new_y] != '*':
        return True


def add_bomb_to_matrix(matrix, bomb_coordinates, positions):
    x, y = map(int, bomb_coordinates[1:-1].split(', '))
    matrix[x][y] = '*'
    for position in positions:
        add_x, add_y = position
        if is_valid_coordinate(matrix, x, y, add_x, add_y):
            matrix[x+add_x][y+add_y] += 1


def print_matrix(matrix):
    [print(' '.join(map(str, row))) for row in matrix]


positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
size = int(input())
matrix = create_matrix(size)
n = int(input())

for _ in range(n):
    bomb = input()
    add_bomb_to_matrix(matrix, bomb, positions)

print_matrix(matrix)