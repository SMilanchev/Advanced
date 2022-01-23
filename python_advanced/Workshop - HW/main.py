import game


def start_game():
    board, current_player, next_player = game.setup()
    moves = []
    no_win = False
    game.loop(board, current_player, next_player, moves, no_win)


start_game()