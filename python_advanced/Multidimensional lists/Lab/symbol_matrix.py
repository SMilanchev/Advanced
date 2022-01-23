def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['X', '!', '@'],
        ]
    size = int(input())
    matirx = []
    for r in range(size):
        row = [x for x in input()]
        matirx.append(row)
    return matirx


def find_symbol_in_matrix(matrix, symbol):
    size = len(matrix)
    for row in range(size):
        if symbol in matrix[row]:
            return (row, matrix[row].index(symbol))


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix()
symbol = input()
print_result(find_symbol_in_matrix(matrix, symbol), symbol)