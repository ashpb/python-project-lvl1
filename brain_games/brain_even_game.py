from random import randint
from brain_games import cli


GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return (number % 2) == 0


def generate_qa_pair():
    number = randint(0, 99)
    even = 'yes' if is_even(number) else 'no'
    return (number, even)


def run():
    cli.welcome()
    print(GAME_DESCRIPTION, '\n')
    name = cli.get_name()
    cli.greet(name)
    print()
    for _ in range(3):
        q, a = generate_qa_pair()
        print('Question: {}'.format(q))
        answer = cli.get_answer()
        if (answer == a):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(answer, a))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
