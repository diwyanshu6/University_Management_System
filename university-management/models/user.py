from enum import Enum


class Role(Enum):

    ADMIN = "ADMIN"
    PROFESSOR = "PROFESSOR"
    STUDENT = "STUDENT"


class User:

    def __init__(self, username, role):

        self.username = username
        self.role = role

    def display_info(self):

        print(
            f"Username: {self.username}\n"
            f"Role: {self.role.value}"
        )