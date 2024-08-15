class HashTable:
    def __init__(self, size):
        # Ініціалізуємо хеш-таблицю з заданим розміром. 
        # Таблиця буде складатися зі списків, кожен з яких відповідає окремому хеш-значенню.
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Хеш-функція, яка генерує індекс для ключа, використовуючи вбудовану функцію hash.
        # Результат хешування ділиться на розмір таблиці для визначення індексу.
        return hash(key) % self.size

    def insert(self, key, value):
        # Вставка ключа та його значення в хеш-таблицю.
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            # Якщо немає списку для цього хеш-значення, створюємо новий.
            self.table[key_hash] = list([key_value])
            return True
        else:
            # Перевіряємо, чи існує вже цей ключ у списку для даного хеш-значення.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    # Якщо ключ вже існує, оновлюємо значення.
                    pair[1] = value
                    return True
            # Якщо ключ не знайдено, додаємо нову пару ключ-значення.
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        # Отримання значення за ключем.
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            # Якщо список існує, шукаємо в ньому пару з відповідним ключем.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        # Якщо ключ не знайдено, повертаємо None.
        return None

    def delete(self, key):
        # Видалення пари ключ-значення з хеш-таблиці.
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            # Якщо список існує, шукаємо в ньому пару з відповідним ключем.
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    # Якщо знайдено відповідний ключ, видаляємо пару.
                    self.table[key_hash].pop(i)
                    return True
        # Якщо ключ не знайдено, повертаємо False.
        return False

# Тестуємо нашу хеш-таблицю з новими значеннями:
H = HashTable(5)
H.insert("apple", 15)
H.insert("orange", 25)
H.insert("banana", 35)
H.insert("grape", 45)
H.insert("peach", 55)

# Отримуємо значення для кожного з ключів
print(H.get("apple"))   # Виведе: 15
print(H.get("orange"))  # Виведе: 25
print(H.get("banana"))  # Виведе: 35
print(H.get("grape"))   # Виведе: 45
print(H.get("peach"))   # Виведе: 55

# Видаляємо деякі ключі
H.delete("orange")
H.delete("banana")

# Перевіряємо, що ключі були видалені
print(H.get("orange"))  # Виведе: None
print(H.get("banana"))  # Виведе: None

# Перевіряємо стан хеш-таблиці після видалення
print(H.table) 
