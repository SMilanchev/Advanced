def read_matrix(is_test=False):
    if is_test:
        return [
            ['0', 'K', '0', 'K', '0'],
            ['K', '0', '0', '0', 'K'],
            ['0', '0', 'K', '0', '0'],
            ['K', '0', '0', '0', 'K'],
            ['0', 'K', '0', 'K', '0'],
        ]
    size = int(input())
    matirx = []
    for r in range(size):
        row = list(input())
        matirx.append(row)
    return matirx


def calculate_kills(matrix, row_index, column_index, knight_moves, size):
    kills = 0
    for (row, col) in knight_moves:
        if 0 <= row_index + row < size and 0 <= column_index + col < size:
            knight = matrix[row_index + row][column_index + col]
            if knight == "K":
                kills += 1
        else:
            continue

    return kills


matrix = read_matrix()
MATRIX_SIZE = len(matrix)
knight_moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
knights_removed = 0
kills = 0


while True:
    max_kills = 0
    killer_position = []

    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if matrix[r][c] == 'K':
                kills = calculate_kills(matrix, r, c, knight_moves, MATRIX_SIZE)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [r, c]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        knights_removed += 1
    else:
        break

print(knights_removed)

