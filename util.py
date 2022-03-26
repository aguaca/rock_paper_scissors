from const import MOVES, RPS
prompt = "{}, {}, {}? > ".format(RPS['rock'], RPS['paper'], RPS['scissors'])


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
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
