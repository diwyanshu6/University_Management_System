class Enrollment:

    def __init__(
        self,
        student_id,
        course_id,
        grade=None,
        enrollment_id=None
    ):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

    def assign_grade(self, grade):
        self.grade = grade