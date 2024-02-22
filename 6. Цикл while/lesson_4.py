print('Урок 4. Бесконечный цикл. Логический тип данных')

count = 10
while count <= 10:
    if count < 0:
        print('Время вышло!')
        break
    else:
        print(count)
        count -= 1

while True:
    work = int(input('Продолжаем работать? 0/1: '))
    if work == 0:
        print('Завершаем работу')
        break

while True:
    print('Компьютер заблокирован. Вернёшь скейт - скажу код разблокировки!')
    code = int(input('Введите код: '))
    if code == 550:
        print('Код верный. Завершаю работу...')
        break