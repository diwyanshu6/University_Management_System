from models.course import Course
from services.authorization_service import (
    AuthorizationService,
    Permission
)


class CourseService:

    def __init__(self, course_repository):

        self.course_repository = course_repository


    def add_course(
        self,
        user,
        course_name,
        professor_id,
        department_id
    ):

        AuthorizationService.check_permission(
            user,
            Permission.ADD_COURSE
        )

        if not course_name.strip():

            raise ValueError(
                "Course name cannot be empty."
            )

        course = Course(
            course_name=course_name,
            professor_id=professor_id,
            department_id=department_id
        )

        return self.course_repository.save(course)


    def get_all_courses(self, user):

        AuthorizationService.check_permission(
            user,
            Permission.VIEW_DATA
        )

        return self.course_repository.find_all()