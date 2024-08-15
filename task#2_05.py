def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return (iterations, upper_bound)

# Приклад використання
arr = [1.1, 2.2, 3.3, 4.4, 5.5]
x = 3.5
print(binary_search(arr, x))  # Наприклад, (3, 4.4)
