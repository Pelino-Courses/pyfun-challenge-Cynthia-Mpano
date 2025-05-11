from person import Person

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, **kwargs):
        # Pass extra kwargs (like employee_id) along the MRO chain
        super().__init__(name, age, **kwargs)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_role(self) -> str:
        return "Student"

    def __iter__(self):
        return iter(self.courses)