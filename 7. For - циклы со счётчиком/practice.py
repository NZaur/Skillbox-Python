# print('Задача 1. Должники')
# for base in range(10):
#     debtor = int(input('Введите номер должника: '))
#     if debtor > 0:
#         if debtor % 2 == 0:
#             print('Пользователя является должником')
#         else:
#             print('Пользователя не является должником')
#     else:
#         print('Число не может быть нулем или отрицательным')


# print('Задача 2. Посчитай чужую зарплату...')
# totalWage = 0
# for month in range(1, 13):
#     print(month, 'месяц')
#     wage = int(input('Введите заплату за текущий месяц: '))
#     totalWage += wage
# print('Средняя зарплата за', month, 'месяцев составляет:', (totalWage // month))


# print('Задача 3. Факториал')
# factorial = 1
# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#     factorial *= i
# print('Факториал числа', n, 'равен:', factorial)


# print('Задача 4. Успеваемость в классе')
# five, four, three = 0, 0, 0
# students = int(input('Введите количество учеников:'))
# for i in range(students):
#     rate = int(input('Введите оценку: '))
#     if rate == 5:
#         five += 1
#     if rate == 4:
#         four += 1
#     else:
#         three += 1
# print('Всего учеников:', students)
# print('Из них Отличников -', five, 'Хорошистов -', four, 'Троечников -', three)


# print('Задача 5. Отрезок')
# a = int(input('Введите начало отрезка: '))
# b = int(input('Введите конец отрезка: '))
# summ = 0
# if a > b:
#     a, b = b, a
# for i in range(a, b + 1):
#     if i % 3:
#         summ += i
# print('Среднее арифметическое всех чисел кратные трем из отрезка равно:', summ // (b - a))


# print('Задача 6. Замечательные числа')
# for i in range(10, 100):
#     if i == (i // 10) * (i % 10) * 3:
#         print('Число', i, 'замечательное')

# print('Задача 7. Пропавшая карточка')
# total_summ_card = 0
# total_card = int(input('Введите количество карт: '))
# for card in range(1, total_card + 1):
#   total_summ_card += card
# for card in range(total_card - 1):
#   lost_card = int(input('Оставшиеся карты: '))
#   total_summ_card -= lost_card
# print('Потерянная карта:', total_summ_card)