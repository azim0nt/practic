

print('Загадайте число! Я попробую его отгадать.')
number = input('---> ')
low = 1
high = 100

while True:
    guess = (low+high) // 2
    player_answer = input(f'Это {guess}? [c/l/h]: ')
    if player_answer == 'c':
        question = input('Хотите ещё раз сыграть? [y/n]: ')
        if question == 'y':
            low = 1
            high = 100
            print('Загадайте число! Я попробую его отгадать.')
            number = input('---> ')
        elif question == 'n':
            print('Приятно было с вами сыграть:)')
            break
    elif player_answer == 'l':
        high = guess -1
    elif player_answer == 'h':
        low = guess +1
    else:
        print('Введите корректный ответ [c/l/h]: ')
        
