from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = [('+', add), ('-', sub), ('*', mul)]


def generate_qa_pair():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    symbol, operation = choice(OPERATIONS)
    expression = "{} {} {}".format(number1, symbol, number2)
    result = str(operation(number1, number2))
    return (expression, result)
