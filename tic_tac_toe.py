from player import Player

class TicTacToe:
    
    def __init__(self):
        self.board = [[0, 0, 0] for i in range(3)]
        self.whos_turn = Player.X

    def play_move(self, row, column):
        if self.board[row][column] != 0:
            raise Exception('This space is already occupided')

        if self.whos_turn == Player.X:
            self.board[row][column] = Player.X.name
            self.whos_turn = Player.O
        else:
            self.board[row][column] = Player.O.name
            self.whos_turn = Player.X

    def print_board(self):
        print('Current Board')
        print('-----')
        for row in self.board:
            print(row[0], row[1], row[2])
        print('-----')