def read_input():
    return [el.strip() for el in input().split('|')[::-1]]


def get_matrix(list):
    return [el.split(' ') for el in list]


def remove_remove_spaces(matrix):
    return [ch for el in matrix for ch in el if ch != ' ']


def print_result(matrix):
    return print(' '.join(matrix))


string = read_input()
matrix = get_matrix(string)
result = remove_remove_spaces(matrix)
print_result(result)
