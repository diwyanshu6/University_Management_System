class Department:

    def __init__(self, name, department_id=None):
        self.department_id = department_id
        self.name = name

    def display_info(self):

        print(
            f"Department ID: {self.department_id}\n"
            f"Name: {self.name}"
        )