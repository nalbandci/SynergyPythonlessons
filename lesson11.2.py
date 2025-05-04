"""Ветеринарная клиника — управление базой данных питомцев

Программа предоставляет CRUD-функционал (Create, Read, Update, Delete) для работы с базой данных питомцев. 
Особенности:
- Автоматическая генерация ID
- Валидация вводимых данных
- Удобный интерфейс с командами
- Корректное склонение возраста

**Команды:**
- `create` — добавить питомца
- `read` — просмотреть информацию
- `update` — изменить данные
- `delete` — удалить запись
- `list` — показать всех питомцев
- `stop` — выход
"""

# Импорт модуля для работы с очередями (нужен для получения последнего ключа)
import collections

# База данных питомцев (ID: {Кличка: {Данные}})
pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}},
}

def get_suffix(age):
    """
    Определяет правильное склонение для возраста.
    Пример: 1 → 'год', 3 → 'года', 25 → 'лет'
    """
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Возвращает данные питомца по ID или False, если не найден"""
    return pets.get(ID, False)

def create():
    """Добавляет новую запись в базу данных"""
    # Генерация нового ID
    if not pets:  # Если база пуста
        new_id = 1
    else:  # Берем последний ID и увеличиваем на 1
        last_id = collections.deque(pets, maxlen=1)[0]
        new_id = last_id + 1

    # Ввод клички
    name = input("Введите кличку питомца: ").strip()

    # Ввод вида с проверкой на цифры
    while True:
        animal_type = input("Введите вид питомца: ").strip()
        if any(char.isdigit() for char in animal_type):
            print("Ошибка: вид не должен содержать цифр!")
        else:
            break

    # Ввод возраста с проверкой
    while True:
        try:
            age = int(input("Введите возраст питомца: "))
            if age < 0:
                print("Ошибка: возраст не может быть отрицательным!")
            else:
                break
        except ValueError:
            print("Ошибка: введите целое число!")

    # Ввод владельца
    owner = input("Введите имя владельца: ").strip()

    # Добавление в базу
    pets[new_id] = {name: {
        "Вид питомца": animal_type,
        "Возраст питомца": age,
        "Имя владельца": owner
    }}
    print(f"Питомец добавлен с ID {new_id}")

def read():
    """Выводит информацию о питомце по ID"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    # Извлечение данных из вложенных словарей
    pet_name = next(iter(pet.keys()))  # Получаем кличку (первый ключ)
    data = pet[pet_name]  # Данные питомца
    age_str = f"{data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}"

    # Форматированный вывод
    print(f'Это {data["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {age_str}. Имя владельца: {data["Имя владельца"]}')

def update():
    """Редактирует существующую запись"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    pet = get_pet(ID)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    pet_name = next(iter(pet.keys()))
    print("Введите новые данные (оставьте пустым, чтобы не изменять):")

    # Обновление вида
    new_type = input(f"Вид питомца ({pet[pet_name]['Вид питомца']}): ").strip()
    if new_type:
        if any(char.isdigit() for char in new_type):
            print("Ошибка: вид не должен содержать цифр!")
        else:
            pet[pet_name]["Вид питомца"] = new_type

    # Обновление возраста
    while True:
        new_age = input(f"Возраст питомца ({pet[pet_name]['Возраст питомца']}): ").strip()
        if not new_age:
            break
        try:
            new_age = int(new_age)
            if new_age < 0:
                print("Ошибка: возраст не может быть отрицательным!")
            else:
                pet[pet_name]["Возраст питомца"] = new_age
                break
        except ValueError:
            print("Ошибка: введите целое число!")

    # Обновление владельца
    new_owner = input(f"Имя владельца ({pet[pet_name]['Имя владельца']}): ").strip()
    if new_owner:
        pet[pet_name]["Имя владельца"] = new_owner

    print("Данные обновлены")

def delete():
    """Удаляет запись из базы"""
    try:
        ID = int(input("Введите ID питомца: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    if ID not in pets:
        print("Питомец с таким ID не найден")
        return

    del pets[ID]
    print("Питомец удален")

def pets_list():
    """Выводит список всех питомцев"""
    if not pets:
        print("База данных пуста")
        return

    for ID, pet in pets.items():
        pet_name = next(iter(pet.keys()))
        data = pet[pet_name]
        age_str = f"{data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}"
        print(f"[ID: {ID}]: {pet_name}, Вид: {data['Вид питомца']}, Возраст: {age_str}, Владелец: {data['Имя владельца']}")

# Основной цикл программы
while True:
    command = input("\nВведите команду (create/read/update/delete/list/stop): ").strip().lower()
    
    if command == "stop":
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print("Неизвестная команда")

print("Работа программы завершена")