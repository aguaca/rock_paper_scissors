from const import MOVES, RPS_COLORS

prompt = "{}, {}, {}? > ".format(
    RPS_COLORS["rock"], RPS_COLORS["paper"], RPS_COLORS["scissors"]
)


def valid_input(prompt=prompt, option=MOVES):
    while True:
        response = input(prompt).lower()
        if response in option:
            break
        else:
            # print("Sorry, I don't understand.")
            pass
    return response


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


def rpsls_beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "rock" and two == "lizard")
        or (one == "scissors" and two == "paper")
        or (one == "scissors" and two == "lizard")
        or (one == "paper" and two == "rock")
        or (one == "paper" and two == "spock")
        or (one == "lizard" and two == "spock")
        or (one == "lizard" and two == "paper")
        or (one == "spock" and two == "rock")
        or (one == "spock" and two == "scissors")
    )
