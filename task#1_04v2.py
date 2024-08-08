import os
import timeit
import random
import heapq

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Знаходимо середину масиву
        left_half = arr[:mid]  # Ліва половина масиву
        right_half = arr[mid:]  # Права половина масиву

        merge_sort(left_half)  # Рекурсивно сортуємо ліву половину
        merge_sort(right_half)  # Рекурсивно сортуємо праву половину

        i = j = k = 0

        # Злиття відсортованих половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Додаємо залишки лівої половини
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Додаємо залишки правої половини
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщуємо елементи масиву, які більші за ключ, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Вставляємо ключ на правильну позицію

def timsort(arr):
    return sorted(arr)  # Використовуємо вбудовану функцію sorted(), яка реалізує Timsort

# Генерація випадкових даних для тестування
def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Вимірювання часу виконання алгоритмів
def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data.copy()), number=1)

sizes = [100, 1000, 5000, 10000]  # Розміри масивів для тестування
results = {}

for size in sizes:
    data = generate_random_list(size)  # Генерація випадкового масиву
    results[size] = {
        'Merge Sort': measure_time(merge_sort, data),  # Вимірювання часу для Merge Sort
        'Insertion Sort': measure_time(insertion_sort, data),  # Вимірювання часу для Insertion Sort
        'Timsort': measure_time(timsort, data),  # Вимірювання часу для Timsort
    }

# Генерація README.md
with open("README.md", "w") as f:
    f.write("# Алгоритми сортування: Ефективність\n\n")
    f.write("Цей проект порівнює ефективність різних алгоритмів сортування: Merge Sort, Insertion Sort та Timsort на випадкових масивах різного розміру.\n\n")
    
    f.write("## Алгоритми сортування\n\n")
    f.write("### Merge Sort\n")
    f.write("Merge Sort — це алгоритм сортування, який використовує принцип розділяй і володарюй. Він ділить масив на дві половини, рекурсивно сортує кожну половину і потім зливає їх в один відсортований масив.\n\n")
    
    f.write("### Insertion Sort\n")
    f.write("Insertion Sort — це простий алгоритм сортування, який працює за принципом вставки. Він проходить через масив і вставляє кожен елемент на його правильне місце.\n\n")
    
    f.write("### Timsort\n")
    f.write("Timsort — це алгоритм сортування, який використовується в стандартній бібліотеці Python. Це гібридний алгоритм, що поєднує Merge Sort і Insertion Sort для досягнення кращої продуктивності.\n\n")
    
    f.write("## Результати тестування\n\n")
    f.write("Тести були проведені на випадкових масивах різного розміру. Ось результати вимірювань часу виконання (у секундах):\n\n")
    f.write("| Розмір масиву | Merge Sort | Insertion Sort | Timsort |\n")
    f.write("|---------------|------------|----------------|---------|\n")
    
    for size in sizes:
        f.write(f"| {size} | {results[size]['Merge Sort']:.6f} | {results[size]['Insertion Sort']:.6f} | {results[size]['Timsort']:.6f} |\n")
    
    f.write("\n## Висновки\n\n")
    f.write("1. **Merge Sort** показує стабільну продуктивність і добре підходить для великих масивів.\n")
    f.write("2. **Insertion Sort** є дуже повільним для великих масивів, оскільки його час виконання зростає квадратично.\n")
    f.write("3. **Timsort** (реалізований вбудованою функцією `sorted()` в Python) є найшвидшим алгоритмом серед трьох, особливо на великих масивах, завдяки своєму гібридному підходу.\n\n")
    
