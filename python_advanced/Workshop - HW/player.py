def create():
    return {}


def player_name(player):
    return player['name']


def player_symbol(player):
    return player['symbol']


def assign_names(*players):
    for i in range(len(players)):
        players[i]['name'] = input(f"Player {i} name:")


def assign_symbols(*players):
    for i in range(len(players)):
        if i == 0:
            players[i]['symbol'] = input(f"{player_name(players[i])} would you like to play with '0' or 'X'?")
        else:
            players[i]['symbol'] = '0' if players[i - 1]['symbol'] == 'X' else 'X'


def has_player_won(board):
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != " ":
        return True
    if (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
        return True
    for row in board:
        if len(set(row)) == 1 and " " not in row:
            return True
    for c in range(len(board)):
        if (board[0][c] == board[1][c] == board[2][c]) and board[0][c] != " ":
            return True


def print_winner(current_player):
    print(f'{player_name(current_player)} wins the game!')


def player_move(current_player):
    return int(input(f"{player_name(current_player)} choose a free position [1-9]: "))
