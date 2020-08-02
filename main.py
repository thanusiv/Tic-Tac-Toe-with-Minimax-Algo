from tic_tac_toe import TicTacToe
from minimax import Mini_Max_Algorithm

def main():
    game = TicTacToe()
    mini_max = Mini_Max_Algorithm()
    while not game.is_over():
        print('\n')
        print('Current Board:')
        game.print_board()
        print(game.whos_turn.name, '\'s turn')
        print('Available Moves:')
        print(game.get_available_moves())
        row = input('Please enter a row: ')
        column = input('Please enter a column: ')
        game.play_move(int(row), int(column))

        if not game.is_over():
            best_value, best_move = mini_max.get_best_move(game, False)
            print('Best Value:', best_value)
            game.play_move(best_move[0], best_move[1])

    print('\n------------------------')
    print('The game is now over!')

    if not game.player_won:
        print('The game was a tie!')
    else:
        print(game.player_won.name, 'won!')

    print('Final Board:')
    game.print_board()


if __name__ == "__main__":
    main()