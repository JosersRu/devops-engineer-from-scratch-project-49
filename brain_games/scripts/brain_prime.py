import random

import brain_games.cli as cli

def is_prime(n: int):
    if (n < 2):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
            

def main():
    name = cli.welcome_user()
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        rand_int = random.randint(1, 100)
        print(f'Question: {rand_int}', end = ' ')
        user_answer = input()
        if (user_answer == 'yes' and is_prime(rand_int) or user_answer == 'no' and not is_prime(rand_int)):
            print(f"Your answer: {user_answer}")
            count += 1
        else:
            print(f'Let\'s try again {name}')
            return

    print(f'Congratulations {name}')
            

if __name__ == "__main__":
    main()
