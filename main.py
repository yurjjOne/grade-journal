"""Журнал оцінок — заліковий проєкт команди (MVP)."""
from src import records as rc
from src.storage import load_json, save_json

DATA_FILE = "journal.json"

MENU = """
=== Журнал оцінок ===
1. Додати оцінку
2. Показати журнал
0. Вийти
"""


def main():
    records = load_json(DATA_FILE, [])
    while True:
        print(MENU)
        choice = input("Ваш вибір: ").strip()
        try:
            if choice == "1":
                student = input("Студент: ")
                subject = input("Предмет: ")
                grade = rc.parse_grade(input("Оцінка (0-100): "))
                rc.add_record(records, student, subject, grade)
                save_json(DATA_FILE, records)
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
