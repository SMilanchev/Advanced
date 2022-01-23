def read_matrix():
    rows_count = int(input())
    return [list(map(int, input().split(', '))) for _ in range(rows_count)]


def get_even_matrix(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]


def print_matrix(matrix):
    print(matrix)


print_matrix(get_even_matrix(read_matrix()))
