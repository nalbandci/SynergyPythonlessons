# Задача: Генерация двух матриц случайными числами с вводом параметров пользователем и их сложение
import random

def create_matrix(rows, cols):
    """Генерирует матрицу заданной размерности со случайными числами от -100 до 100"""
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    """Складывает две матрицы одинаковой размерности"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Ошибка: матрицы имеют разный размер!")
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

# Приветствие и ввод данных
print("🌐 Программа для генерации и сложения матриц 🌐")
print("• Введите размеры матриц •")

# Ввод размеров с проверкой
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Ошибка: число должно быть больше 0!")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число!")

rows = get_positive_integer("Количество строк: ")
cols = get_positive_integer("Количество столбцов: ")

# Генерация матриц
print("\n🔷 Генерирую первую матрицу...")
matrix_1 = create_matrix(rows, cols)
print("✅ Первая матрица создана!")

print("\n🔷 Генерирую вторую матрицу...")
matrix_2 = create_matrix(rows, cols)
print("✅ Вторая матрица создана!")

# Вывод сгенерированных матриц
def print_matrix(matrix, name):
    print(f"\n📊 Матрица {name}:")
    for i, row in enumerate(matrix, 1):
        print(f"Строка {i:2}: {', '.join(map(str, row))}")

print_matrix(matrix_1, "A")
print_matrix(matrix_2, "B")

# Сложение матриц и вывод результата
print("\n🧮 Складываю матрицы...")
try:
    matrix_3 = add_matrices(matrix_1, matrix_2)
    print_matrix(matrix_3, "результат сложения (A + B)")
except ValueError as e:
    print(f"\n❌ {e}")

print("\n" + "="*50 + "\n✅ Операция завершена!")