"""
Программа создает иерархию классов для моделирования транспорта.
1. Родительский класс Transport хранит базовые характеристики:
   - название транспорта (name)
   - максимальная скорость (max_speed)
   - пробег (mileage)
2. Дочерний класс Autobus наследует все свойства и методы Transport.
3. Создается объект автобуса с конкретными параметрами.
4. Выводится информация о транспорте в заданном формате.
"""

# Создаем родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name          # Название транспорта
        self.max_speed = max_speed  # Максимальная скорость (км/ч)
        self.mileage = mileage    # Пробег (тыс. км)

# Создаем дочерний класс Autobus, наследующийся от Transport
class Autobus(Transport):
    pass  # Наследуем все атрибуты и методы без изменений

# Создаем объект автобуса с параметрами из задания
autobus = Autobus(name="Renaul Logan", max_speed=180, mileage=12)

# Форматированный вывод информации о транспорте
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")