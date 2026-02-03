import random
from math import gcd

import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        result = gcd(num1, num2)
        print(f'Question: {num1} {num2}', end = ' ')
        user_answer = input()
        if (user_answer == str(result)):
            count += 1
            print(f'You answer: {user_answer} \nCorrect!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f'Let\'s try again {name}')
            return

    print(f'Congratulations {name}')
    

if __name__ == "__main__":
    main()
