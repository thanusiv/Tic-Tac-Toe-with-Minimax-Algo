from tic_tac_toe import TicTacToe
from minimax import Minimax_Algorithm

def main():
    game = TicTacToe()
    mini_max = Minimax_Algorithm()
    while not game.is_over():
        print('\n')
        print('Current Board:')
        game.print_board()
        print(game.whos_turn.name, '\'s turn')
        print('Available Moves:')
        print(game.get_available_moves())
        
        valid = False
        while not valid:
            try:
                row = input('Please enter a row: ')
                column = input('Please enter a column: ')
                game.play_move(int(row), int(column))
                valid = True
            except Exception as e:
                print(e)

        if not game.is_over():
            best_value, best_move = mini_max.get_best_move(game, False)
            print('Best Value:', best_value)
            game.play_move(best_move[0], best_move[1])

    print('\n------------------------')
    print('The game is now over!')

    if not game.player_won:
        print('It was a tie!')
    else:
        print(game.player_won.name, 'won!')

    print('Final Board:')
    game.print_board()


if __name__ == "__main__":
    main()