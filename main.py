"""Журнал оцінок — заліковий проєкт команди (MVP)."""

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
                print("Додавання запису з'явиться в наступній версії.")
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
