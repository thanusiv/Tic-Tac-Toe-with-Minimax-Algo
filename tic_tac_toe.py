from player import Player

class TicTacToe:
    
    def __init__(self):
        self.board = [[0, 0, 0] for i in range(3)]
        self.whos_turn = Player.X
        self.available_moves = [[x, y] for x in range(3) for y in range(3)]
        self.game_over = False
        self.player_won = None

    def play_move(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise Exception('Invalid move')
        elif not self.available_moves:
            raise Exception('No more possibele moves to complete. This game is over')
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

    def is_game_over(self):
        if len(self.available_moves) > 4:
            return False
        elif not self.available_moves: # no more moves
            return True
        
        # Check for row wins
        for row in range(3):
            possible_player_to_win = self.board[row][0]
            if possible_player_to_win == 0:
                continue
            row_win = True
            for column in range(1,3):
                if self.board[row][column] != possible_player_to_win:
                    row_win = False
                    break
            if row_win:
                self.player_won = Player.X if possible_player_to_win == 'X' else Player.O
                return True 

        # Check for column wins
        for column in range(3):
            possible_player_to_win = self.board[0][column]
            if possible_player_to_win == 0:
                continue
            column_win = True
            for row in range(1,3):
                if self.board[row][column] != possible_player_to_win:
                    column_win = False
                    break
            if column_win:
                self.player_won = Player.X if possible_player_to_win == 'X' else Player.O
                return True

        # Check for left to right diagonal win
        possible_player_to_win = self.board[0][0]
        if self.board[1][1] == possible_player_to_win and self.board[2][2] == possible_player_to_win:
            self.player_won = Player.X if possible_player_to_win == 'X' else Player.O
            return True

        # Check for right to left diagonal win
        possible_player_to_win = self.board[0][2]
        if self.board[1][1] == possible_player_to_win and self.board[2][0] == possible_player_to_win:
            self.player_won = Player.X if possible_player_to_win == 'X' else Player.O
            return True
        
        return False # if no other case is True, it must be False
