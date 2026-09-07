from models.professor import Professor
from services.authorization_service import (
    AuthorizationService,
    Permission
)


class ProfessorService:

    def __init__(self, professor_repository):

        self.professor_repository = professor_repository


    def add_professor(
        self,
        user,
        name,
        email,
        specialization,
        department_id
    ):

        AuthorizationService.check_permission(
            user,
            Permission.ADD_PROFESSOR
        )

        if not name.strip():

            raise ValueError(
                "Professor name cannot be empty."
            )

        professor = Professor(
            name=name,
            email=email,
            specialization=specialization,
            department_id=department_id
        )

        return self.professor_repository.save(
            professor
        )


    def get_all_professors(self, user):

        AuthorizationService.check_permission(
            user,
            Permission.VIEW_DATA
        )

        return self.professor_repository.find_all()