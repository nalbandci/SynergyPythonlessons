
"""
Класс Черепашка для симуляции перемещений.


"""
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # Текущая координата X
        self.y = y  # Текущая координата Y
        self.s = s  # Размер шага (s >= 1)

    def go_up(self):
        """Двигаться вверх по оси Y."""
        self.y += self.s

    def go_down(self):
        """Двигаться вниз по оси Y."""
        self.y -= self.s

    def go_left(self):
        """Двигаться влево по оси X."""
        self.x -= self.s

    def go_right(self):
        """Двигаться вправо по оси X."""
        self.x += self.s

    def evolve(self):
        """Увеличить размер шага на 1."""
        self.s += 1

    def degrade(self):
        """Уменьшить размер шага. При s <= 0 вызывает ошибку."""
        if self.s <= 1:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """Вычисляет минимальное количество шагов до точки (x2, y2)."""
        dx = abs(x2 - self.x)  # Разница по X
        dy = abs(y2 - self.y)  # Разница по Y
        # Вычисляем шаги для каждой оси с округлением вверх
        steps_x = (dx + self.s - 1) // self.s if dx != 0 else 0
        steps_y = (dy + self.s - 1) // self.s if dy != 0 else 0
        return steps_x + steps_y  # Общее количество шагов

"""
Пояснение к классу Turtle:
1. __init__: задает стартовую позицию (x, y) и размер шага s.
2. Методы go_up/down/left/right: меняют координаты на s единиц.
3. evolve/degrade: управляют размером шага с проверкой на s > 0.
4. count_moves: вычисляет минимальные шаги через деление с округлением вверх.
"""


# Пример использования класса Turtle
turtle = Turtle(0, 0, 2)
turtle.go_right()  # x = 2
turtle.go_up()     # y = 2
print(turtle.count_moves(5, 3))  # Минимум 3 шага (по X: (5-2)/2=1.5 → 2 шага; по Y: (3-2)/2=0.5 → 1 шаг)
turtle.evolve()    # s = 3
print(turtle.count_moves(5, 3))  # Теперь 1 шаг по X и 0 по Y → 1 шаг