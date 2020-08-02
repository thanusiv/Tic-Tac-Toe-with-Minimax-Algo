from player import Player

class TicTacToe:
    
    def __init__(self):
        self.board = [[0, 0, 0] for i in range(3)]
        self.whos_turn = Player.X
        self.available_moves = [[x, y] for x in range(3) for y in range(3)]

    def play_move(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise Exception('Invalid move')
        elif self.board[row][column] != 0:
            raise Exception('This space is already occupied')

        self.available_moves.remove([row, column])

        if self.whos_turn == Player.X:
            self.board[row][column] = Player.X.name
            self.whos_turn = Player.O
        else:
            self.board[row][column] = Player.O.name
            self.whos_turn = Player.X

    def print_board(self):
        print('Current Board |', self.whos_turn.name, '\'s turn')
        print('-----')
        for row in self.board:
            print(row[0], row[1], row[2])
        print('-----')

    def get_available_moves(self):
        return self.available_moves
