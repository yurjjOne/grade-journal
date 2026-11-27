"""Тести журналу оцінок (python test_records.py)."""
import os
import tempfile

from src import records as rc
from src.storage import load_json, save_json

assert rc.parse_grade(" 95 ") == 95
for bad in ("abc", "101", "-1", "9.5"):
    try:
        rc.parse_grade(bad)
        raise AssertionError(bad)
    except rc.InvalidGradeError:
        pass

data = []
rc.add_record(data, "Олена", "Математика", 90)
rc.add_record(data, "Олена", "Фізика", 80)
rc.add_record(data, "Іван", "Математика", 70)
try:
    rc.add_record(data, "  ", "Фізика", 50)
    raise AssertionError("порожнє ім'я")
except ValueError:
    pass
assert rc.average_by_student(data) == {"Олена": 85.0, "Іван": 70.0}
assert rc.format_records(data)[0] == "Іван — Математика: 70"

with tempfile.TemporaryDirectory() as folder:
    path = os.path.join(folder, "j.json")
    save_json(path, data)
    assert load_json(path, []) == data
    assert load_json(os.path.join(folder, "none.json"), []) == []

print("Усі тести пройдено")
