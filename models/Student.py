from models.Person import Person
from models.Course import Course

class Student(Person):
     def __init__(self, name: str, age: int, phone: str, courses: list[Course]) -> None:
        super().__init__(name, age, phone)
        self.courses = courses