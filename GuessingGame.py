import random

system_number = random.randrange(1, 100)
attempts = 0
play = True

print('Привет! Давай сыграем в игру - компьютер загадывает число, а ты должен отгадать.')
while play:
    print('Введите число от 1 до 100:')
    user_number = int(input())
    attempts += 1

    if user_number > system_number:
        print('Загаданное число меньше введённого. Попробуйте ещё раз.')
        continue
    elif user_number < system_number:
        print('Загаданное число больше введённого. Попробуйте ещё раз.')
        continue
    else:
        print('Поздравляю, вы победили!\nВам потребовалось попыток:', attempts,
              '\nХотите сыграть ещё? y/n')

        playAgain = input()
        if playAgain.lower() == 'y':
            system_number = random.randrange(1, 100)
            continue
        else:
            print('Спасибо за игру!')
            play = False
