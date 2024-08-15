import timeit
import time
import re

# Функція для обчислення поліноміального хешу рядка
def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

# Алгоритм Рабіна-Карпа для пошуку підрядка
def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

# Функція для створення таблиці зсувів для алгоритму Боєра-Мура
def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

# Алгоритм Боєра-Мура для пошуку підрядка
def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i  # Підрядок знайдено, повертаємо перший знайдений індекс

        # Зсув індексу i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1

# Функція для обчислення префіксної функції для алгоритму Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

# Алгоритм Кнута-Морріса-Пратта для пошуку підрядка
def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

# Функція для пошуку підрядка за допомогою регулярних виразів


def regex_search(main_string, pattern):
    # Екрануємо спеціальні символи, щоб уникнути помилок у регулярних виразах
    pattern = re.escape(pattern)
    match = re.search(pattern, main_string)
    if match:
        return match.start()
    else:
        return -1


# Функція для зчитування тексту з файлу
def read_file(file_path):
    # Пробуємо зчитати файл з кодуванням 'utf-8'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Якщо 'utf-8' не спрацювало, пробуємо з 'cp1251'
        with open(file_path, 'r', encoding='cp1251') as file:
            return file.read()


# Функція для вимірювання часу виконання пошуку підрядка
def measure_search_time(func, text, pattern):
    setup_code = f'''from __main__ import {func.__name__}'''
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=10)

# Зчитування текстів з файлів
text1 = read_file("article1.txt")
text2 = read_file("article2.txt")

# Визначення підрядків для пошуку
existing_substring = "Стаття"  # Підрядок, який дійсно існує в тексті
fake_substring = "Свій вигаданий рядок тут :)"  # Вигаданий підрядок

if __name__ == '__main__':

    # Вимірювання часу виконання
    for i, text in enumerate([text1, text2]):
        print(f"\nСтаття №{i+1}")
        results = []
        for pattern in [existing_substring, fake_substring]:
            for search_func in [boyer_moore_search, kmp_search, rabin_karp_search, regex_search]:
                time = measure_search_time(search_func, text, pattern)
                results.append((search_func.__name__, pattern, time))

        # Виведення результатів у вигляді таблиці
        print(f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час (секунди)':<15}")
        print('-' * 80)
        for result in results:
            print(f"{result[0]:<30} | {result[1]:<30} | {result[2]:<15.5f}")

    # Додатковий приклад, який був у кінці коду
    s = [(0, "a"), (1, "b"), (2, "c")]
    for e in s:
        print(e)
