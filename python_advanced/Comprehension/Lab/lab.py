def are_coordinates_valid(matrix, row, column):
    size = len(matrix)
    return 0 <= row < size and 0 <= column < size


if are_coordinates_valid([1, 2, 3], 2, 3):
    print('Yes')
# print(are_coordinates_valid([1, 2, 3], 2, 1))