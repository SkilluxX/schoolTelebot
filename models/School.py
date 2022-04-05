from models.Course import Course
from models.Person import Person


class School:
    def __init__(self, name: str, courses: list[Course], employees: list[Person]):
        self.name = name
        self.courses = courses
        self.employees = employees

    def displayInfo(self) -> str:
        info = ""
        info += f"Название {self.name}\nНаправления: \n"
        for course in self.courses:
            info += course.display() + "\n"

        info += "Сотрудники: \n"
        for emp in self.employees:
            info += emp.display() + "\n"

        return info