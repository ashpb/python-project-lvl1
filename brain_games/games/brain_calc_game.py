from random import randint, choice
from brain_games import game_flow

GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_qa_pair():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = choice(['+', '-', '*'])
    expression = "{} {} {}".format(number1, operation, number2)
    calc_funcs = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y}
    result = str(calc_funcs.get(operation)(number1, number2))
    return (expression, result)


def run():
    game_flow.run(GAME_DESCRIPTION, generate_qa_pair)
