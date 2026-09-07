from models.person import Person
class Student(Person):

    def __init__(
        self,
        name,
        email,
        student_id=None,
        department_id=None
    ):
        super().__init__(name, email)

        self.student_id = student_id
        self.department_id = department_id

    def display_info(self):

        print(
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Department ID: {self.department_id}"
        )