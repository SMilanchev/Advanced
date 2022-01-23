
def print_board(board):
    [print(f"| {' | '.join(el)} |") for el in board]


def create_board(is_start=False):
    if is_start:
        print('This is the numeration of the board:')
        return [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
        ]
    else:
        return [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]


def add_move_to_board(board, move, symbol, moves):
    length = len(board)
    if move % length == 0:
        c = length-1
        r = (move // 3) - 1
    else:
        c = (move % 3) - 1
        r = move // 3
    board[r][c] = symbol
    moves.append(move)
