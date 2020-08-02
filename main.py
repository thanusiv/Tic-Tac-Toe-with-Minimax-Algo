from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    game.print_board()
    game.play_move(0, 1)
    game.print_board()
    game.play_move(0,2)
    game.print_board()
    print(game.get_available_moves())


if __name__ == "__main__":
    main()