# Программа для проверки, является ли строка палиндромом.

# Вводим строку без пробелов
input_string = input("Введите строку: ")

# Проверка, является ли строка палиндромом
if input_string == input_string[::-1]:  # Сравниваем строку с её реверсированной версией
    print("yes")  # Если строки совпадают, выводим "yes"
else:
    print("no")   # Если строки не совпадают, выводим "no"