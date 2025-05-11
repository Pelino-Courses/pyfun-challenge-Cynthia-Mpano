class Course:
    def __init__(self, title: str, course_code: str, credits: int):
        self.title = title
        self.course_code = course_code
        self.credits = credits
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        student.enroll(self)

    def __add__(self, other):
        return Course(
            title=f"{self.title} & {other.title}",
            course_code=f"{self.course_code}-{other.course_code}",
            credits=self.credits + other.credits
        )

    def __iter__(self):
        return iter(self.students)