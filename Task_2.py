from collections import deque

def is_palindrome(s):
    # Нормалізація рядка: переведення у нижній регістр та видалення пробілів
    normalized_str = ''.join(s.lower().split())
    
    # Створення двосторонньої черги з символів нормалізованого рядка
    char_deque = deque(normalized_str)
    
    # Порівняння символів з обох кінців, поки черга не стане порожньою
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Рядок не є паліндромом
    return True  # Рядок є паліндромом


# Приклади використання
print(is_palindrome("Madam"))  # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))  # False
