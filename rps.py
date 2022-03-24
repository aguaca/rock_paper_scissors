#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
GREEN = "\u001b[32;1m"
ORANGE = "\u001b[33m"
PURPLE = "\u001b[35;1m"
RESET = "\u001b[0m"
rps = {
    "rock": GREEN + 'Rock' + RESET,
    "paper": ORANGE + 'Paper' + RESET,
    "scissors": PURPLE + 'Scissors' + RESET
}

"""The Player class is the parent class for all of the Players
in this game"""


def valid_input(prompt="{}, {}, {}? > ".format(rps['rock'],rps['paper'],rps['scissors'])):
    while True:
        response = input(prompt).lower()
        if response in moves:
            break
        else:
            # print("Sorry, I don't understand.")
            pass
    return response


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        return valid_input()


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        return self.last_move

    def learn(self, _, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        i = moves.index(self.last_move) + 1
        if i < len(moves):
            return moves[i]
        else:
            return moves[0]

    def learn(self, my_move, _):
        self.last_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You played {}.".format(rps[move1].lower()))
        print("Opponent played {}.".format(rps[move2].lower()))

        result = beats(move1, move2)
        if move1 == move2:
            print("\u001b[41;1m** TIE **\u001b[0m")
        elif result:
            print("\u001b[45m** PLAYER ONE WINS **\u001b[0m")
            self.score1 += 1
        else:
            print("\u001b[46;1m** PLAYER TWO WINS **\u001b[0m")
            self.score2 += 1

        print(f"Score: Player One {self.score1}, Player Two {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\u001b[7mGame start!\u001b[0m")
        for round in range(5):
            print(f"Round {round + 1} --\n")
            self.play_round()
        print('\n\x1b[6;30;42m' + 'Last Round, Game Over!' + '\x1b[0m')


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
