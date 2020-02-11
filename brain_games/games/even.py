from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return (number % 2) == 0


def generate_qa_pair():
    number = randint(0, 100)
    even = 'yes' if is_even(number) else 'no'
    return (number, even)
