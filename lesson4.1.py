# Нужно написать скрипт, который принимает от пользователя
# стороны прямоугольника и выводит площадь и периметр.
# При этом пользователь может вводить как целые числа, так и вещественные.

# Ввод сторон прямоугольника
a = float(input("Введите длину стороны a:"))
b = float(input("Введите длину стороны b:"))

# Вычисление площади и периметра
area = a * b
perimeter = 2 * (a+b)

# вывод резултатов
print(f"Площадь: {area}")
print(f"Периметр: {perimeter}")