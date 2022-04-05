
from models.Course import Course
from models.School import School
from models.Teacher import Teacher

class Application:
    courses = [
    Course("Python", 800, 40),
    Course("C#", 800, 30)
    ]

    emp = [
        Teacher("Алексей Бородин", 19, "+7-909-079-15-65", courses)
    ]

    school = School("Школа", courses, emp)