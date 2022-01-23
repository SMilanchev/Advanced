def read_matrix():
    matrix = []
    for _ in range(8):
        row = input().split(' ')
        matrix.append(row)

    return matrix


def check_rows(matrix, current_row, current_col):
    queens_coords = []
    row = matrix[current_row]
    if "Q" in row:
        for i in range(current_col-1, -1, -1):
            if row[i] == "Q":
                queens_coords.append([current_row, i])
                break
        for m in range(current_col + 1, 8):
            if row[m] == "Q":
                queens_coords.append([current_row, m])
                break
    return queens_coords


def check_cols(matrix, current_row, current_col):
    queens_coords = []
    for i in range(current_row - 1, -1, -1):
        if matrix[i][current_col] == "Q":
            queens_coords.append([i, current_col])
            break
    for m in range(current_row + 1, 8):
        if matrix[m][current_col] == "Q":
            queens_coords.append([m, current_col])
            break
    return queens_coords


def vaalidate_coord(x):
    if 0 <= x <= 7:
        return True


def check_diagonals(matrix, current_row, current_col):
    queens_coords = []
    curr_col = current_col
    for r in range(current_row - 1, -1, -1):
        curr_col -= 1
        if vaalidate_coord(curr_col):
            if matrix[r][curr_col] == "Q":
                queens_coords.append([r, curr_col])
                break
    curr_col = current_col
    for r in range(current_row - 1, -1, -1):
        curr_col -= 1
        if vaalidate_coord(curr_col):
            if matrix[r][curr_col] == "Q":
                queens_coords.append([r, curr_col])
                break
    curr_col = current_col
    for r in range(current_row + 1, 8):
        curr_col -= 1
        if vaalidate_coord(curr_col):
            if matrix[r][curr_col] == "Q":
                queens_coords.append([r, curr_col])
                break
    curr_col = current_col
    for r in range(current_row + 1, 8):
        curr_col -= 1
        if vaalidate_coord(curr_col):
            if matrix[r][curr_col] == "Q":
                queens_coords.append([r, curr_col])
                break

    return queens_coords


def print_result(result):
    for el in result:
        if not el:
            print('The king is safe!')
            break
        else:
            print(el)


matrix = read_matrix()
queens_coords = []
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "K":
            queens_coords.append(check_rows(matrix, row, col))
            queens_coords.append(check_cols(matrix, row, col))
            queens_coords.append(check_diagonals(matrix, row, col))

print_result(queens_coords)