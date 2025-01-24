import random


lives = 3

while True:

    if lives <= 0:
        print('У вас не осталось попыток')
        question = input('Хотите ещё раз сыграть? [y/n]: ')
        if question == 'y':
            random_number = random.randint(1,100)
            lives = 3
            continue
        elif question == 'n':
            print('Приятно было с вами сыграть:)')
            break
    else:
        random_number = random.randint(1,100)
        print('Old number: ', random_number)
        print('Попробуйте угадать число от 1 до 100: ')
        player_number = input('---> ')
        
        
        if player_number.isdigit():
            if int(player_number) == random_number:
                print('Вы угадали число')
                question = input('Хотите ещё раз сыграть? [y/n]: ')
                if question == 'y':
                    random_number = random.randint(1,100)
                    lives = 3
                    continue
                elif question == 'n':
                    print('Приятно было с вами сыграть:)')
                    break
                
            else:
                lives -= 1
                random_number = random.randint(1,100)
                print(f'Неправильно! У вас осталось {lives} попыток') 
        