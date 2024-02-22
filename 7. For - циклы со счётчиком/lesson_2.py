print('7.2 Цикл for. Работа со списком чисел')

# for number in range(1, 11):
#     print(number ** 2)

# winners = 0
# for tickets in 345, 19, 87, 1020, 421, 555:
#     if tickets % 5 == 0:
#         print(tickets, '- счастливый билет!')
#         winners += 1
# print('Количество победителей:', winners)

# for meters in  100,90,95,87,102:
#  if meters % 3 == 0:
#    print(meters, 'Подходит')
#  else:
#    print(meters, 'Не подходит')

# for numb in 3, 7, 5, 6, 4:
#     print(numb ** 2, numb ** 3, numb ** 4)

winners = 0
for ticket in 345, 19, 87, 1020, 421, 670, 223, 435, 100, 1000:
    if 99 < ticket < 1000:
        if ticket % 5 == 0:
            print(ticket, '- выигрышный билет!')
            winners += 1
print('Всего победителей:', winners)
