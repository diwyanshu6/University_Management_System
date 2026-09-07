from models.student import Student
from services.authorization_service import (
    AuthorizationService,
    Permission
)


class StudentService: 

    def __init__(self, student_repository):

        self.student_repository = student_repository


    def add_student(
        self,
        user,
        name,
        email,
        department_id
    ):

        AuthorizationService.check_permission(
            user,
            Permission.ADD_STUDENT
        )

        if not name.strip():

            raise ValueError(
                "Student name cannot be empty."
            )

        if not email.strip():

            raise ValueError(
                "Student email cannot be empty."
            )

        student = Student(
            name=name,
            email=email,
            department_id=department_id
        )

        return self.student_repository.save(student)


    def get_student(self, user, student_id):

        AuthorizationService.check_permission(
            user,
            Permission.VIEW_DATA
        )

        return self.student_repository.find_by_id(
            student_id
        )


    def get_all_students(self, user):

        AuthorizationService.check_permission(
            user,
            Permission.VIEW_DATA
        )

        return self.student_repository.find_all()


    def delete_student(self, user, student_id):

        AuthorizationService.check_permission(
            user,
            Permission.DELETE_STUDENT
        )

        return self.student_repository.delete(
            student_id
        )