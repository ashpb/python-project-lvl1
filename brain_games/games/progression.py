from random import randint

DESCRIPTION = 'What number is missing in the progression?'
LENGTH = 10


def generate_qa_pair():
    first = randint(0, 10)
    step = randint(1, 10)
    missing_index = randint(0, LENGTH - 1)
    progession = [first + (i * step) for i in range(LENGTH)]
    expression = " ".join([str(val) if idx != missing_index else '..'
                           for idx, val in enumerate(progession)])
    result = str(progession[missing_index])
    return (expression, result)
