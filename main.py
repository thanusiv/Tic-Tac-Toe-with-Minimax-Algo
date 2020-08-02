from tic_tac_toe import TicTacToe
from minimax import Mini_Max_Algorithm

def main():
    game = TicTacToe()
    mini_max = Mini_Max_Algorithm()
    while not game.is_over():
        game.print_board()
        print('Available Moves:')
        print(game.get_available_moves())
        row = input('Please enter a row: ')
        column = input('Please enter a column: ')
        game.play_move(int(row), int(column))
        print('\n')
        if not game.is_over():
            best_value, best_move = mini_max.get_best_move(game, False)
            print('Best Value:', best_value)
            game.play_move(best_move[0], best_move[1])


if __name__ == "__main__":
    main()