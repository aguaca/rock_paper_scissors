#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def valid_input(prompt="Rock, paper, scissors? > "):
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
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")

        result = beats(move1, move2)
        if move1 == move2:
            print("** TIE **")
        elif result:
            print("** PLAYER ONE WINS **")
            self.score1 += 1
        else:
            print("** PLAYER TWO WINS **")
            self.score2 += 1

        print(f"Score: Player One {self.score1}, Player Two {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1} --")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
