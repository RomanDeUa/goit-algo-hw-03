import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності вхідних параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    # Генерація унікальних випадкових чисел у заданому діапазоні
    numbers = random.sample(range(min, max + 1), quantity)
    # Повернення відсортованого списку чисел
    return sorted(numbers)

# Приклади використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

# Перевірка для некоректних параметрів
lottery_numbers = get_numbers_ticket(5, 3, 6)
print("Некоректні параметри:", lottery_numbers)
