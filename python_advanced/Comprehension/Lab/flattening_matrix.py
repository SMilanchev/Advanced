def read_matrix():
    rows_count = int(input())
    rows = [input().split(', ') for _ in range(rows_count)]
    return rows


matrix = read_matrix()
print([int(x) for line in matrix for x in line])