print('Урок 6: Оператор continue в цикле while')

number = int(input('Введите число: '))
while number >= 0:          # Обратный отсчет
    if number == 3:         # Если число 3
        number -= 1         # Убавляем число на 1
        continue            # Возвращаемся в начало цикла
        break               # Игнорируем break
    print(number)
    number -= 1