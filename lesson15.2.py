"""
Программа демонстрирует переопределение методов в наследовании.
1. Родительский класс Transport содержит метод seating_capacity(), 
   который принимает вместимость как аргумент.
2. Дочерний класс Autobus переопределяет этот метод, задавая 
   значение по умолчанию для параметра capacity = 50.
3. Создается объект автобуса и вызывается метод с демонстрацией 
   работы переопределенной логики.
"""

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name          # Название транспорта
        self.max_speed = max_speed  # Максимальная скорость (км/ч)
        self.mileage = mileage    # Пробег (тыс. км)

    def seating_capacity(self, capacity):
        # Базовый метод для отображения вместимости
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        # Переопределенный метод с значением по умолчанию
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Создаем объект автобуса
autobus = Autobus(name="Renaul Logan", max_speed=180, mileage=12)

# Вызываем метод без указания capacity - используем значение по умолчанию
print(autobus.seating_capacity())