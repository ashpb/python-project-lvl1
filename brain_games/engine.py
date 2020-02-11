from brain_games import cli


def run(game):
    cli.welcome()
    print(game.DESCRIPTION, '\n')
    name = cli.get_name()
    cli.greet(name)
    print()
    for _ in range(3):
        q, a = game.generate_qa_pair()
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
