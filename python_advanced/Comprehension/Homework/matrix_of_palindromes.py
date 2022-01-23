def print_result(result):
    return [print(' '.join(element)) for element in result]


(rows, columns) = map(int, input().split(' '))
matrix = [[f'{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}' for c in range(columns)] for r in range(rows)]

print_result(matrix)