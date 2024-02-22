print('7.1 Разбор домашнего задания')

numb = int(input('Загадай число от 1 до 100: '))
left_border = 1
right_border = 100
attempt = 0
while True:
    check = (left_border + right_border) // 2
    attempt += 1
    if check > numb:
        print('Мое число меньше', check)
        right_border = check
    elif check < numb:
        print('Мое число больше', check)
        left_border = check
    elif check == numb:
        print('Угадал за', attempt, 'попыток! Твое число', check)
        break