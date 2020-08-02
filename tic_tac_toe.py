class TicTacToe:
    
    def __init__(self):
        self.board = [[0, 0, 0] for i in range(3)]
    
    def play_move(self, player, row, column):
        if self.board[row][column] != 0:
            raise Exception('This space is already occupided')

        if player == 'X':
            self.board[row][column] = player
        else:
            self.board[row][column] = player

    def print_board(self):
        print('Current Board')
        print('-----------')
        for row in self.board:
            print(row)
        print('-----------')