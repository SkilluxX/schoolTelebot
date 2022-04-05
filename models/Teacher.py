from models.Person import Person
from models.Course import Course


class Teacher(Person):
    def __init__(self, name: str, age: int, phone: str, courses: list[Course]) -> None:
        super().__init__(name, age, phone)
        self.courses = courses

    def display(self):
        return f"{self.name}: {self.phone}"