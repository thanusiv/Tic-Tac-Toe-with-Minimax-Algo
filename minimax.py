from player import Player
from copy import deepcopy

class Mini_Max_Algorithm:
    def __init__(self):
        self.maximizing_player = Player.X
        self.minimizing_player = Player.O
        self.infinity = float('Inf')
    
    def get_best_move(self, game, is_maxmizing):
        if game.is_over():
            return [self.evaluate_game(game), '']
        
        best_move = [None, None]

        if is_maxmizing:
            best_value = -self.infinity
            player = self.maximizing_player
        else:
            best_value = self.infinity
            player = self.minimizing_player

        for move in game.get_available_moves():
            new_hypothetical_game = deepcopy(game)
            new_hypothetical_game.play_move(move[0], move[1])
            hypothetical_best_value = self.get_best_move(new_hypothetical_game, not is_maxmizing)[0]

            if is_maxmizing:
                if hypothetical_best_value > best_value:
                    best_value = hypothetical_best_value
                    best_move = move
            else:
                if hypothetical_best_value < best_value:
                    best_value = hypothetical_best_value
                    best_move = move
        
        return [best_value, best_move]

    def evaluate_game(self, game):
        if game.player_won == self.maximizing_player:
            return self.infinity
        elif game.player_won == self.minimizing_player:
            return -self.infinity
        else:
            return 0
