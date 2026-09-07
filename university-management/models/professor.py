from models.person import Person


class Professor(Person):

    def __init__(
        self,
        name,
        email,
        specialization,
        professor_id=None,
        department_id=None
    ):
        super().__init__(name, email)

        self.professor_id = professor_id
        self.specialization = specialization
        self.department_id = department_id

    def display_info(self):

        print(
            f"Professor ID: {self.professor_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Specialization: {self.specialization}\n"
            f"Department ID: {self.department_id}"
        )