def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],
        ]
    (rows, cols) = map(int, input().split(' '))
    matirx = []
    for r in range(rows):
        row = input().split(' ')
        matirx.append(row)
    return matirx


def find_squares(matrix):
    squares_counter = 0
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[r]) - 1):
            current_char = matrix[r][c]
            if current_char == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
                squares_counter += 1
    return squares_counter


matrix = read_matrix()
print(find_squares(matrix))