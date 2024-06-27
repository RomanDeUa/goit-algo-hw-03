from datetime import datetime

def get_days_from_today(date_string):
    try:
        # Перетворюємо рядок у об'єкт datetime
        target_date = datetime.strptime(date_string, '%Y-%m-%d').date()
        
        # Отримуємо поточну дату
        today = datetime.today().date()
        
        # Розраховуємо різницю у днях між поточною датою та заданою датою
        delta = today - target_date
        
        # Повертаємо різницю у днях як ціле число
        return delta.days
    except ValueError:
        # Якщо формат дати неправильний, повертаємо повідомлення про помилку
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

# Приклади використання функції
print(get_days_from_today("2021-10-09"))  # Повинно повернути 157, якщо сьогодні 5 травня 2021 року
print(get_days_from_today("2024-06-25"))  # Відповідно до поточної дати (наприклад, якщо сьогодні 26 червня 2024 року)
print(get_days_from_today("2020-10-09"))  # Відповідно до поточної дати (наприклад, якщо сьогодні 26 червня 2024 року)
print(get_days_from_today("2021-02-30"))  # Повинно повернути повідомлення про помилку через неправильний формат дати

