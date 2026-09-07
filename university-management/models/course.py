class Course:

    def __init__(
        self,
        course_name,
        course_id=None,
        professor_id=None,
        department_id=None
    ):
        self.course_id = course_id
        self.course_name = course_name
        self.professor_id = professor_id
        self.department_id = department_id

    def display_info(self):

        print(
            f"Course ID: {self.course_id}\n"
            f"Course: {self.course_name}\n"
            f"Professor ID: {self.professor_id}\n"
            f"Department ID: {self.department_id}"
        )