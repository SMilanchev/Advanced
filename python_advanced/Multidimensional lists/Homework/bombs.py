def read_matrix(is_test=False):
    if is_test:
        return [
            [8, 3, 2, 5],
            [6, 4, 7, 9],
            [9, 9, 3, 6],
            [6, 8, 1, 2],

        ]
    size = int(input())
    matirx = []
    for r in range(size):
        row = list(map(int, input().split(' ')))
        matirx.append(row)
    return matirx


def is_point_valid(row, column, size):
    if 0 <= row < size and 0 <= column < size and matrix[row][column] > 0:
        return True
    else:
        return False


def get_bomb_exploded(matrix, bomb_row, bomb_column, points_affected):
    size = len(matrix)
    current_bomb = matrix[bomb_row][bomb_column]
    if current_bomb > 0:
        matrix[bomb_row][bomb_column] -= current_bomb
        for point in points_affected:
            if is_point_valid(bomb_row + point[0], bomb_column + point[1], size):
                matrix[bomb_row + point[0]][bomb_column + point[1]] -= current_bomb

    return matrix


def final_result(bomb_coordinates):
    for bomb in bomb_coordinates:
        bomb_row, bomb_column = map(int, bomb.split(','))
        get_bomb_exploded(matrix, bomb_row, bomb_column, points_affected_by_bomb)

    alive_cells = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 0:
                alive_cells.append(matrix[r][c])
    return matrix, alive_cells


def print_result(result):
    matrix, alive_cells = result
    print(f'Alive cells: {len(alive_cells)}')
    print(f'Sum: {sum(alive_cells)}')
    for line in matrix:
        print(' '.join(str(x) for x in line))


matrix = read_matrix(is_test=False)
bomb_coordinates = input().split(' ')
points_affected_by_bomb = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
print_result(final_result(bomb_coordinates))
