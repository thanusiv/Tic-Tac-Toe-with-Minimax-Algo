from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    while not game.is_game_over():
        game.print_board()
        print('Available Moves:')
        print(game.get_available_moves())
        row = input('Please enter a row: ')
        column = input('Please enter a column: ')
        game.play_move(int(row), int(column))


if __name__ == "__main__":
    main()