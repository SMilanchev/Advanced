def read_matrix(is_test=False):
    if is_test:
        return [
                   ['*', '*', '*', 'c', '*'],
                   ['*', '*', '*', 'e', '*'],
                   ['*', '*', 'c', '*', '*'],
                   ['s', '*', '*', 'c', '*'],
                   ['*', '*', 'c', '*', '*'],
               ], ['up', 'right', 'right', 'up', 'right']
    size = int(input())
    commands = input().split(' ')
    matirx = []
    for r in range(size):
        row = input().split(' ')
        matirx.append(row)
    return matirx, commands


def get_miner_current_position(matrix, miner_place='s'):
    for row in range(len(matrix)):
        if miner_place in matrix[row]:
            column = matrix[row].index(miner_place)
            return row, column


def validate_command(matrix, current_row, current_column, row, column):
    size = len(matrix)
    if 0 <= current_row + row < size and 0 <= current_column + column < size:
        return True
    else:
        return False


def miner_movement(matrix, command, commands_dict):
    row, column = get_miner_current_position(matrix)
    if validate_command(matrix, row, column, commands_dict[command][0], commands_dict[command][1]):
        return (row + commands_dict[command][0], column + commands_dict[command][1])
    return row, column


def are_coals_remaining(matrix, coal_sign='c'):
    for el in matrix:
        if coal_sign in el:
            return True
    return False


def coals_remaining(matrix):
    size = len(matrix)
    counter = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'c':
                counter += 1
    return counter


matrix, commands = read_matrix(is_test=False)
commands_dict = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
coal_counter = 0
game_over = False
current_position = - 2
new_position = - 3


for command in commands:
    current_position = get_miner_current_position(matrix)
    new_position = miner_movement(matrix, command, commands_dict)

    if current_position != new_position:
        if matrix[new_position[0]][new_position[1]] == '*':
            matrix[current_position[0]][current_position[1]] = '*'
            matrix[new_position[0]][new_position[1]] = 's'
        elif matrix[new_position[0]][new_position[1]] == 'e':
            print(f'Game over! {new_position}')
            game_over = True
            break
        elif matrix[new_position[0]][new_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            matrix[new_position[0]][new_position[1]] = 's'
            coal_counter += 1
    else:
        continue

if not are_coals_remaining(matrix) and not game_over:
    print(f'You collected all coals! {new_position}')
if not game_over and are_coals_remaining(matrix):
    remaining_coals = coals_remaining(matrix)
    print(f'{remaining_coals} coals left. {new_position}')