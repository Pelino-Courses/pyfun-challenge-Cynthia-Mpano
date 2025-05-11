from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, age: int, student_id: str, employee_id: str):
        # Call super().__init__ once, passing both student_id and employee_id as keyword arguments.
        super().__init__(name, age, student_id=student_id, employee_id=employee_id)

    def get_role(self) -> str:
        return "Teaching Assistant"