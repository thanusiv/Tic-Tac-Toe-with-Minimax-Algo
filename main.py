from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    game.print_board()
    game.play_move(0, 1)
    game.print_board()


if __name__ == "__main__":
    main()