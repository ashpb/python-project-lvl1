from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def generate_qa_pair():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = choice([('+', add), ('-', sub), ('*', mul)])
    expression = "{} {} {}".format(number1, operation[0], number2)
    result = str(operation[1](number1, number2))
    return (expression, result)
