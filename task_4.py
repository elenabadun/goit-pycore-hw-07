# Завдання 4
"""
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе
вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день
народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача
та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також
повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

Вимоги до завдання:
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок)
та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день.
Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name)
та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').

Рекомендації для виконання:
Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday
(дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків
у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"],
"%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
Визначте поточну дату системи за допомогою datetime.today().date().
Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте
дату на наступний рік.
Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження
відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.

Критерії оцінювання:
Актуальність та коректність визначення днів народження на 7 днів вперед.
Правильність обробки випадків, коли дні народження припадають на вихідні.
Читабельність та структурованість коду.

Приклад:
Припустимо, у вас є список users:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Використання функції get_upcoming_birthdays:
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

Якщо сьогодні 2024.01.22 результатом може бути:
[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'},
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.
"""


from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    This function takes one parameter - the list users.
    First, we get the current date, and then the function iterates through the list of users to find their
    birthdays in the current year.
    It also identifies users whose birthdays fall within the next 7 days.
    If a birthday falls on a weekend, the function moves the congratulation date to the nearest Monday.
    Finally, it returns a ready list of congratulation dates for the current week.
    """

    today = datetime.today().date()

    birthday_this_year = today.year

    formated_dates = []
    for user in users:
        formated_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        formated_date = formated_date.replace(year=birthday_this_year)
        if formated_date < today:
            formated_date = formated_date.replace(year=birthday_this_year + 1)
        if formated_date >= today and formated_date < today + timedelta(days=7):
            if formated_date.weekday() == 5:
                formated_date = formated_date + timedelta(days=2)
            if formated_date.weekday() == 6:
                formated_date = formated_date + timedelta(days=1)
            formated_dates.append(
                {
                    "name": user["name"],
                    "congratulation_date": formated_date.strftime("%Y.%m.%d"),
                }
            )

    return formated_dates


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Elizabet Stone", "birthday": "1995.03.23"},
    {"name": "Ellie Dill", "birthday": "2001.03.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
