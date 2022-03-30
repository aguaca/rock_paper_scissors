import random
from const import MOVES, RPS_COLORS
from util import valid_input
from time import sleep


class Player:
    def __init__(self, game_mode):
        self.game_mode = game_mode

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self, game_mode):
        super().__init__(game_mode)

    def move(self):
        if self.game_mode == "1":
            return random.choice(MOVES)
        else:
            return random.choice(MOVES + ["lizard", "spock"])


class HumanPlayer(Player):
    def __init__(self, game_mode):
        super().__init__(game_mode)

    def move(self):
        if self.game_mode == "1":
            return valid_input()
        else:
            prompt = "{}, {}, {}, {}, {}? > ".format(
                RPS_COLORS["rock"],
                RPS_COLORS["paper"],
                RPS_COLORS["scissors"],
                RPS_COLORS["lizard"],
                RPS_COLORS["spock"],
            )
            return valid_input(prompt, MOVES + ["lizard", "spock"])


class ReflectPlayer(Player):
    def __init__(self, game_mode):
        super().__init__(game_mode)
        # Ternary operator
        moves = MOVES if game_mode == "1" else MOVES + ["lizard", "spock"]
        self.last_move = random.choice(moves)

    def move(self):
        return self.last_move

    def learn(self, _, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self, game_mode):
        super().__init__(game_mode)
        # Ternary operator
        self.moves = MOVES if game_mode == "1" else MOVES + ["lizard", "spock"]
        self.last_move = random.choice(self.moves)

    def move(self):
        i = self.moves.index(self.last_move) + 1
        if i < len(self.moves):
            return self.moves[i]
        else:
            return self.moves[0]

    def learn(self, my_move, _):
        self.last_move = my_move
