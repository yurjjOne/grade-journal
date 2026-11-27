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
