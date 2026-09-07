from models.enrollment import Enrollment
from services.authorization_service import (
    AuthorizationService,
    Permission
)


class EnrollmentService:

    def __init__(self, enrollment_repository):

        self.enrollment_repository = enrollment_repository


    def enroll_student(
        self,
        user,
        student_id,
        course_id
    ):

        AuthorizationService.check_permission(
            user,
            Permission.ENROLL_COURSE
        )

        enrollment = Enrollment(
            student_id=student_id,
            course_id=course_id
        )

        return self.enrollment_repository.save(
            enrollment
        )


    def assign_grade(
        self,
        user,
        enrollment_id,
        grade
    ):

        AuthorizationService.check_permission(
            user,
            Permission.ASSIGN_GRADE
        )

        if grade not in [
            "A+",
            "A",
            "B+",
            "B",
            "C",
            "D",
            "F"
        ]:

            raise ValueError(
                "Invalid grade."
            )

        return self.enrollment_repository.assign_grade(
            enrollment_id,
            grade
        )


    def get_enrollments(self, user):

        AuthorizationService.check_permission(
            user,
            Permission.VIEW_DATA
        )

        return self.enrollment_repository.find_all()