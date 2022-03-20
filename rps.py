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
            print("Sorry, I don't understand.")
    return response


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2): 
        self.p1 = p1
        self.p2 = p2

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
        else:
            print("** PLAYER TWO WINS **")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round} --")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()