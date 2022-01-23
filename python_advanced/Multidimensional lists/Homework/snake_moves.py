rows, columns = map(int, input().split(' '))
word = input()

matrix = []
for r in range(rows):
    matrix.append([0 for el in range(columns)])

index_word = 0

for row_index in range(rows):
    for col_index in range(columns):
        matrix[row_index][col_index] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for r in range(rows):
    if r % 2 == 1:
        matrix[r].reverse()
    print(''.join(matrix[r]))

