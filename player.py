import random
from const import MOVES
from util import valid_input


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)


class HumanPlayer(Player):
    def move(self):
        return valid_input()


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = random.choice(MOVES)

    def move(self):
        return self.last_move

    def learn(self, _, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = random.choice(MOVES)

    def move(self):
        i = MOVES.index(self.last_move) + 1
        if i < len(MOVES):
            return MOVES[i]
        else:
            return MOVES[0]

    def learn(self, my_move, _):
        self.last_move = my_move
