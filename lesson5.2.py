"""
Задача: Подсчёт гласных и согласных в слове.
Дано слово из маленьких латинских букв. 
Требуется определить количество гласных и согласных букв, 
а также вывести количество каждой из гласных ('a', 'e', 'i', 'o', 'u'). 
Если гласная отсутствует, вывести False.
"""



# Вводим слово
word = input("Введите слово из маленьких латинских букв: ")

# Определяем гласные буквы
vowels = {'a', 'e', 'i', 'o', 'u'}

# Считаем количество гласных и согласных
vowel_count = 0
consonant_count = 0

# Словарь для подсчета каждой гласной
vowel_counts = {vowel: 0 for vowel in vowels}

# Проходим по каждой букве в слове
for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_counts[letter] += 1
    else:
        consonant_count += 1

# Выводим результаты
print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")

# Проверяем наличие каждой гласной и выводим их количество
for vowel, count in vowel_counts.items():
    if count == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {count}")
