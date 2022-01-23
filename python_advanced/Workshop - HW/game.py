import player
import board_actions



def setup():
    player_1 = player.create()
    player_2 = player.create()

    player.assign_names(player_1, player_2)
    player.assign_symbols(player_1, player_2)

    game_board = board_actions.create_board(is_start=True)
    board_actions.print_board(game_board)

    current_player = player_1
    next_player = player_2

    print(f"{player.player_name(current_player)} starts first!")
    return board_actions.create_board(is_start=False), current_player, next_player


def is_move_valid(move, moves, size):
    if move not in moves and 1 <= move <= 3 * size:
        return True


def no_winner(moves):
    if len(set(moves)) == 9:
        print("Nobody wins. Start the game again.")
        return True


def game_move(current_player):
    move = int(input(f"{current_player['name']} choose a free position [1-9]: "))


def loop(board, current_player, next_player, moves, no_win=False):
    while not player.has_player_won(board):
        if no_winner(moves):
            no_win = True
            break
        move = player.player_move(current_player)
        if is_move_valid(move, moves, 3):
            board_actions.add_move_to_board(board, move, player.player_symbol(current_player), moves)
            board_actions.print_board(board)
            current_player, next_player = next_player, current_player
        else:
            print('Invalid position. Try again')
    if not no_win:
        player.print_winner(next_player)
