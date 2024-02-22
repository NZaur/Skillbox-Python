print('7.4 Функция range с началом отсчёта')

# begin_number = int(input('Введите начальное число: '))
# end_number = int(input('Введите конечное число: '))
# for number in range(begin_number, end_number + 1):
#     print(number ** 2)

# wake_up = int(input('Во сколько проснулся: '))
# awake_hours = 0
# calories_sum = 0
# for hours in range(wake_up, 23):
#     print('Сейчас', hours, 'часов')
#     calories = int(input('Сколько съел за час: '))
#     calories_sum += calories
#     if calories_sum > 2000:
#         print('Хорошо поел. Можно и поспать')
#         break
#     awake_hours += 1
# print('Съедено калорий за день:', calories)
# print('Часов не спал:', awake_hours)

# for i in range(1, 11):
#     print(i ** 3)

# first_numb = int(input('Введите первое число: '))
# second_numb = int(input('Введите второе число (больше первого): '))
# totalSumm = 0
# for summ in range(first_numb, second_numb + 1):
#     totalSumm += summ
# print('Сумма чисел от', first_numb, 'до', second_numb, 'равна', totalSumm)

# wake_up = int(input('Во сколько проснулся: '))
# totalCalories = 0
# awake_hours = 0
# for hours in range(wake_up, 23):
#     print('Сейчас', hours, 'часов')
#     calories = int(input('Введите количество съеденных за этот час калорий: '))
#     totalCalories += calories
#     if totalCalories > 2000:
#         print('Пора спать')
#         break
#     awake_hours += 1
# print('Общее время бодрствования:', awake_hours)
# print('Калорий съедено:', totalCalories)