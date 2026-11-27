"""Збереження журналу у JSON-файл."""
import json


def load_json(path, default):
    """Прочитати JSON; немає файлу або файл пошкоджений — повернути default."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        print(f"Файл {path} пошкоджений, починаємо з порожнього журналу.")
        return default


def save_json(path, data):
    """Записати дані у JSON (кирилиця читабельна, відступ 2)."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
