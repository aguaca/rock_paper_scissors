#!/usr/bin/env python3
from const import H_GREEN, RPS_COLORS, RESET, H_RED, H_PINK, H_BLUE, H_REVERSED
import player as p
from util import beats, rpsls_beats, valid_input

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
        # check if player one is an instance of the HumanPlayer subclass
        if isinstance(self.p1, p.HumanPlayer):
            print("You played {}.".format(RPS_COLORS[move1].lower()))
            print("Opponent played {}.".format(RPS_COLORS[move2].lower()))
        else:
            print("Computer played {}.".format(RPS_COLORS[move1].lower()))
            print("Opponent played {}.".format(RPS_COLORS[move2].lower()))

        if self.p1.game_mode == "1":
            result = beats(move1, move2)
        else:
            result = rpsls_beats(move1, move2)

        if move1 == move2:
            print(f"{H_RED}** TIE **{RESET}")
        elif result:
            print(f"{H_PINK}** PLAYER ONE WINS **{RESET}")
            self.score1 += 1
        else:
            print(f"{H_BLUE}** PLAYER TWO WINS **{RESET}")
            self.score2 += 1

        print(f"Score: Player One {self.score1}, Player Two {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print(f"{H_REVERSED}Rock Paper Scissors, Go!{RESET}")
        for round in range(rounds):
            print(f"\nRound {round + 1} --")
            self.play_round()
        print("\n" + H_GREEN + "Last Round, Game Over!" + RESET)


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
            print("___________________________")
        else:
            player = get_player("Select Player 2: ")

        return player

    def start_game(self):
        print("(1) rps")
        print("(2) rpsls")
        game_mode = valid_input("Select a game mode: ", ["1", "2"])

        print("___________________________")
        player1 = self._select_player()
        player2 = self._select_player(player2=True)
        print("___________________________")
        rounds = valid_input(
            "Number of rounds? (1-10): ", [f"{x}" for x in range(1, 11)]
        )
        game = Game(player1(game_mode), player2(game_mode))
        game.play_game(int(rounds))


if __name__ == "__main__":
    menu = Menu()
    menu.start_game()
