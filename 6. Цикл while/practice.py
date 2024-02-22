print('Урок 7: Практическая работа')

# number = int(input('Введите число: '))
# number_count = 1
# while number_count <= number:
#      result = number_count ** 3
#      print(number_count, 'в степени 3 будет', result)
#      number_count += 1

# name = input('Введите имя должника: ')
# debt = int(input('Введите сумму долга: '))
# activity = 0
# while debt > activity:
#      print(name + ', Ваша задолженность составляет', debt, 'рублей!')
#      activity = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить: '))
#      if debt <= activity:
#           break
#      ('Маловато,', name + '. Давайте ещё раз.')
#      debt -= activity
# print('Отлично,', name + '! Вы погасили долг. Спасибо!')

# numb = int(input('Введите число: '))
# last_numb = numb % 10  # Берем крайнюю цифру числа
# numb_count = 0  # Счетчик цифр
# while numb != 0:  # Пока число не станет 0
#     numb //= 10  # Убираем крайнюю цифру числа
#     numb_count += 1  # Добавляем единицу в счетчик
# print('Количество десятичных цифр (знаков):', numb_count)

# positive = 0
# negative = 0
# review = int(input('Введите оценку от -100 до 100: '))
# while review != 0:
#      if review > 0:
#           positive += 1
#      else:
#           negative += 1
#      review = int(input('Введите оценку от -100 до 100: '))
# print('Количество положительных отзывов:', positive)
# print('Количество отрицательных отзывов:', negative)

# hours_count = 1
# total_tasks = 0
# print('Начался 8-часовой рабочий день')
# while hours_count <= 8:
#     print(hours_count, 'час работы')
#     tasks = int(input('Сколько задач решит Максим? '))
#     total_tasks += tasks
#     hours_count += 1
#     call = int(input('Звонит жена. Взять трубку? '))
#     if call == 1:
#         call_check = True
# print('Рабочий день закончился. Выполнено задач:', total_tasks)
# if call_check == True:
#     print('Нужно зайти в магазин')

# years = 0
# deposit = int(input('Введите сумму вклада: '))
# percent = int(input('Введите желаемый процент: '))
# goal = int(input('Какой размер вклада Вы планируете получить: '))
#
# while deposit < goal:
#     print('Влад на текущий момент:', deposit)
#     income = deposit * percent // 100
#     deposit += income
#     print('Влад после начисления процентов:', deposit)
#     years += 1
# print('Ваш вклад составляет:', deposit)
# print('Лет копился:', years)

# secret_numb = int(input('Загадай число: '))
# check_numb = int(input('Введи число: '))
# counter = 1
# while check_numb != secret_numb:
#     counter += 1
#     if check_numb > secret_numb:
#         print('Число больше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
#     check_numb = int(input('Введи число: '))
# print('Вы угадали! Число попыток:', counter)

# numb = int(input('Загадай число от 1 до 100: '))
# left_border = 1
# right_border = 100
# attempt = 0
# while True:
#     check = (left_border + right_border) // 2
#     attempt += 1
#     if check > numb:
#         print('Мое число меньше', check)
#         right_border = check
#     elif check < numb:
#         print('Мое число больше', check)
#         left_border = check
#     elif check == numb:
#         print('Угадал за', attempt, 'попыток! Твое число', check)
#         break
