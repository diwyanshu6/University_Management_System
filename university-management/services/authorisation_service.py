from enum import Enum


class Permission(Enum):

    ADD_STUDENT = "ADD_STUDENT"
    DELETE_STUDENT = "DELETE_STUDENT"

    ADD_PROFESSOR = "ADD_PROFESSOR"

    ADD_COURSE = "ADD_COURSE"

    ENROLL_COURSE = "ENROLL_COURSE"

    ASSIGN_GRADE = "ASSIGN_GRADE"

    VIEW_DATA = "VIEW_DATA"


class AuthorizationService:

    ROLE_PERMISSIONS = {

        "ADMIN": {
            Permission.ADD_STUDENT,
            Permission.DELETE_STUDENT,
            Permission.ADD_PROFESSOR,
            Permission.ADD_COURSE,
            Permission.VIEW_DATA
        },

        "PROFESSOR": {
            Permission.VIEW_DATA,
            Permission.ASSIGN_GRADE
        },

        "STUDENT": {
            Permission.VIEW_DATA,
            Permission.ENROLL_COURSE
        }
    }

    @staticmethod
    def has_permission(user, permission):

        permissions = AuthorizationService.ROLE_PERMISSIONS.get(
            user.role.value,
            set()
        )

        return permission in permissions

    @staticmethod
    def check_permission(user, permission):

        if not AuthorizationService.has_permission(
            user,
            permission
        ):
            raise PermissionError(
                f"Role {user.role.value} "
                f"does not have permission "
                f"{permission.value}"
            )