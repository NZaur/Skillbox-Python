print('Задача 1. Пропавшая переменная')
# Что нужно сделать
# Найдите в программе необъявленную переменную и объявите её, присвоив ей значение ‘Кот’.

client, pet = 'Петя', 'Кот'
print(client, 'и', pet)

print('\n' + '=' * 75 + '\n')

print('Задача 2. Цвета')
r, g, b = 'Red', 'Green', 'Blue'
print(r, b, g, r + g + b, b, g + b)

print('\n' + '=' * 75 + '\n')

print('Задача 3. Животные')
first_animal, second_animal = 'Заяц', 'Черепаха'
print(first_animal, 'спит,', second_animal, 'идет')

print('\n' + '=' * 75 + '\n')

print('Задача 4. Информация о пользователе')
name, surname = input('Введите имя: '), input('Введите фамилию: ')
print('Вас зовут:', name, surname)
name, surname, city = input('Введите имя: '), input('Введите фамилию: '), input('Введите город проживания: ')
print('Вас зовут:', name, surname + '.', 'Вы живёте в городе:', city)

print('\n' + '=' * 75 + '\n')

print('Задача 5. Вход в систему')
first_name = input('Введите имя пользователя: ')
greeting = 'Утро доброе'
print(greeting, first_name)
print("К сожалению, у Вас нет доступа к системе.")
print("Пожалуйста, обратитесь к системному администратору.")

print('\n' + '=' * 75 + '\n')

print('Задача 6. Полёт')
out_city, in_city = input('Введите город вылета: '), input('Введите город прилета: ')
print(out_city, '-', in_city)

print('\n' + '=' * 75 + '\n')

print('Задача 7. Путь к файлу')
user, file_name = input('Введите свое имя: '), input('Введите имя файла: ')
print('C:/' + user + '/docs/folder/' + file_name + '.txt')

print('\n' + '=' * 75 + '\n')

print('Задача 8. Обмен значений двух переменных')
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
c = a
a = b
b = c
print(a, b)
