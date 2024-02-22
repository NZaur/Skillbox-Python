print('Урок 3: Прерывание цикла, оператор break')

weather = int(input('Сколько градусов на улице? '))
meters: int = 0
while weather > 15:
    meters += 20
    weather -= 2
    if weather <= 15:
        break
    meters += 10
print('Пройдено метров:', meters)


number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_num = number % 10
    print(last_num)
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    summ += last_num
    number //= 10
print('Сумма:', summ)

number = int(input('Введите число: '))
count = 0
while number >= 0:
    print('Число положительное или нуль')
    number = int(input('Введите число: '))
    count += 1
print('Число отрицательное. Количество введенных чисел:', count + 1)

balance = int(input('Введите начальный баланс: '))
while balance < 10000:
    cube = int(input('Сколько выпало на кубике? '))
    if cube != 3:
        print('Выиграли 500 рублей!')
        balance += 500
    else:
        print('Вы проиграли всё!')
        balance = 0
        break
print('Игра закончена.')
print('Итого осталось:', balance)