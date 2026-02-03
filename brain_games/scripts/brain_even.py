import random

import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        rand_int = random.randint(1, 100)
        print(f'Question: {rand_int}', end=' ')
        user_answer = input()
        if (
            rand_int % 2 == 0 and user_answer == 'yes' 
            or
            rand_int % 2 != 0 and user_answer == 'no'):
            
            count += 1
            print(f'You answer: {user_answer} \nCorrect!')
        else:
            print(f'Let\'s try again {name}')
            return

    print(f'Congratulations {name}')
            

if __name__ == "__main__":
    main()
