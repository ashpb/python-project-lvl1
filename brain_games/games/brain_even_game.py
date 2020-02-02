from random import randint
from brain_games import game_flow

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return (number % 2) == 0


def generate_qa_pair():
    number = randint(0, 99)
    even = 'yes' if is_even(number) else 'no'
    return (number, even)


def run():
    game_flow.run(GAME_DESCRIPTION, generate_qa_pair)
