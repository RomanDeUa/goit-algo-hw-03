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

# Приклад використання функції
print(get_days_from_today("2021-10-09"))  # Повинно повернути 157, якщо сьогодні 5 травня 2021 року

