#!/usr/bin/env python3
from const import RPS
import player as p
from util import beats, valid_input

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You played {}.".format(RPS[move1].lower()))
        print("Opponent played {}.".format(RPS[move2].lower()))

        result = beats(move1, move2)
        if move1 == move2:
            print("\u001b[41;1m** TIE **\u001b[0m")
        elif result:
            print("\u001b[45m** PLAYER ONE WINS **\u001b[0m")
            self.score1 += 1
        else:
            print("\u001b[44;1m** PLAYER TWO WINS **\u001b[0m")
            self.score2 += 1

        print(f"Score: Player One {self.score1}, Player Two {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print("\n\u001b[7mRock Paper Scissors, Go!\u001b[0m")
        for round in range(rounds):
            print(f"\nRound {round + 1} --")
            self.play_round()
        print("\n\x1b[6;30;42m" + "Last Round, Game Over!" + "\x1b[0m")


class Menu:
    def __init__(self):
        self.players = {
            "random": p.RandomPlayer,
            "cycle": p.CyclePlayer,
            "human": p.HumanPlayer,
            "reflect": p.ReflectPlayer,
        }

    # Abstraction
    def _select_player(self, player2=False):
        players = ["random", "cycle", "human", "reflect"]

        if player2:
            players.remove("human")

        for i, player in enumerate(players):
            print(f"({i+1}) {player}")

        def get_player(prompt):
            # List comprehension
            player = valid_input(
                prompt, [f"{x+1}" for x, _ in enumerate(players)]
            )
            # Casting
            player = players[int(player) - 1]
            print(f"player selected: {player}")
            return self.players[player]

        # List comprehension
        if not player2:
            player = get_player("Select Player 1: ")
            print("_____________________________")
        else:
            player = get_player("Select Player 2: ")

        return player

    def start_game(self):
        player1 = self._select_player()
        player2 = self._select_player(player2=True)
        print("_____________________________")
        rounds = valid_input(
            'Number of rounds? ("1-10"): ',
            [f"{x}" for x in range(10) if x != 0],
        )
        game = Game(player1(), player2())
        game.play_game(int(rounds))


if __name__ == "__main__":
    menu = Menu()
    menu.start_game()
