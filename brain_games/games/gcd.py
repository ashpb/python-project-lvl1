from random import randint
from math import gcd
from brain_games import game_flow

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_qa_pair():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    expression = "{} {}".format(number1, number2)
    result = str(gcd(number1, number2))
    return (expression, result)


def run():
    game_flow.run(GAME_DESCRIPTION, generate_qa_pair)
