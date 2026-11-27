"""Журнал оцінок: запис = {"student": ..., "subject": ..., "grade": ...}."""


class InvalidGradeError(ValueError):
    """Оцінка некоректна."""


def parse_grade(text):
    """Ціле число від 0 до 100, інакше InvalidGradeError."""
    try:
        grade = int(text.strip())
    except ValueError:
        raise InvalidGradeError(f"«{text}» не є цілим числом")
    if not 0 <= grade <= 100:
        raise InvalidGradeError("оцінка має бути від 0 до 100")
    return grade


def add_record(records, student, subject, grade):
    """Додати запис; порожнє ім'я або предмет -> ValueError."""
    student = student.strip()
    subject = subject.strip()
    if student == "" or subject == "":
        raise ValueError("ім'я студента і предмет не можуть бути порожніми")
    records.append({"student": student, "subject": subject, "grade": grade})


def format_records(records):
    """Рядки для виводу журналу, відсортовані за студентом і предметом."""
    lines = []
    for r in sorted(records, key=lambda r: (r["student"], r["subject"])):
        lines.append(f"{r['student']} — {r['subject']}: {r['grade']}")
    return lines


def average_by_student(records):
    """Словник {студент: середній бал}."""
    sums = {}
    counts = {}
    for r in records:
        sums[r["student"]] = sums.get(r["student"], 0) + r["grade"]
        counts[r["student"]] = counts.get(r["student"], 0) + 1
    return {name: sums[name] / counts[name] for name in sums}
