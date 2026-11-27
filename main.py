"""Журнал оцінок — заліковий проєкт команди (MVP)."""
from src import records as rc

MENU = """
=== Журнал оцінок ===
1. Додати оцінку
2. Показати журнал
0. Вийти
"""


def main():
    records = []
    while True:
        print(MENU)
        choice = input("Ваш вибір: ").strip()
        try:
            if choice == "1":
                student = input("Студент: ")
                subject = input("Предмет: ")
                grade = rc.parse_grade(input("Оцінка (0-100): "))
                rc.add_record(records, student, subject, grade)
                print("Запис додано.")
            elif choice == "2":
                print("Показ журналу з'явиться в наступній версії.")
            elif choice == "0":
                print("До побачення!")
                break
            else:
                print("Невідомий пункт меню.")
        except ValueError as error:
            print("Помилка:", error)


if __name__ == "__main__":
    main()
