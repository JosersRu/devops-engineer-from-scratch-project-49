import random

import brain_games.cli as cli


def main():
    name = cli.welcome_user()
    count = 0
    print('What number is missing in the progression?')
    while count != 3:
        len = 10
        step = random.randint(1,10) 
        start = random.randint(1,50)
        progression = [start + step * i for i in range(len)]        
        hidden_index = random.randrange(len)
        
        result = progression[hidden_index]
        progression[hidden_index] = ".."
        
        print("Question: ", ' '.join(map(str, progression)), end = ' ')
        user_answer = input()
        if (user_answer == str(result)): 
            count += 1
            print(f"Your answer {user_answer} \nCorrect!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'.")
            return
        
    print(f'Congratulations {name}')
    

if __name__ == "__main__":
    main()
