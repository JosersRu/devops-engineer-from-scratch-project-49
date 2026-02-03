import random

import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    count = 0
    print('What is the result of the expression?')
    while count != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        expression = f"{num1} {operation} {num2}"
        result = eval(expression)
        print(f'Question: {expression}?')
        user_answer = input()
        if (user_answer == str(result)):
            
            count += 1
            print(f'Your answer: {user_answer} \n Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct anwser was "{result}"')
            print(f'Let\'s try again {name}!')
            return

    print(f'Congratulations {name}')
            

if __name__ == "__main__":
    main()
