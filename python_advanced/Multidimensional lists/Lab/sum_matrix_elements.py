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


matrix = read_matrix()

sum = 0
for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        sum += row[c]

print(sum)
print(matrix)