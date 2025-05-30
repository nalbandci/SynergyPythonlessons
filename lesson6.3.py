# напишем программу, которая принимает два целых числа A и B, причем гарантируется, 
# что A ≤ B. Затем нужно вывести все четные числа на этом отрезке через пробел.


# Вводим целые числа A и B
A = int(input("Введите целое число A: "))  # Пользователь вводит начальное число A
B = int(input("Введите целое число B: "))  # Пользователь вводит конечное число B

# Проверка условия A ≤ B
if A > B:
    print("Ошибка: A не может быть больше B.")  # Сообщение об ошибке
else:
    # Создаем список для хранения четных чисел
    even_numbers = []

    # Перебираем числа от A до B
    for number in range(A, B + 1):  # Цикл проходит по всем числам от A до B включительно
        if number % 2 == 0:  # Проверяем, является ли число четным
            even_numbers.append(number)  # Если число четное, добавляем его в список

    # Выводим все четные числа через пробел
    print("Четные числа на заданном отрезке:", ' '.join(map(str, even_numbers)))