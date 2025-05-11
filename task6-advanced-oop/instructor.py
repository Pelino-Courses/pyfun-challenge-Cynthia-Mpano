from person import Person

class Instructor(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_role(self) -> str:
        return "Instructor"