print('Урок 2: Оператор while')

password = int(input('Введите пароль: '))
while password != 235:
    print('Неверный пароль!')
    password = int(input('Попробуйте еще раз: '))
print('Пароль верный! Добро пожаловать!')

balance = int(input('Сколько денег пришло?  '))
while balance > 5000:
    product_cost = int(input('Введите стоимость товара: '))
    balance -= product_cost
print('Внимание! На карте осталось мало денег! Остановитесь!')
print('Баланс счета:', balance)

total = 0
number = int(input('Введите число: '))
while number != 0:
    total += number
    number = int(input('Введите число: '))
print(total)

number = 0
while number < 98:
    number += 7
    print(number)