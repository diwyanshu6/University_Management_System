from database.db import Database
from models.professor import Professor


class ProfessorRepository:

    def save(self, professor):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO professors
            (name, email, specialization, department_id)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            professor.name,
            professor.email,
            professor.specialization,
            professor.department_id
        )

        cursor.execute(query, values)

        connection.commit()

        professor.professor_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return professor


    def find_all(self):

        connection = Database.get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        query = """
            SELECT *
            FROM professors
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        professors = []

        for row in rows:

            professors.append(
                Professor(
                    name=row["name"],
                    email=row["email"],
                    specialization=row["specialization"],
                    professor_id=row["professor_id"],
                    department_id=row["department_id"]
                )
            )

        return professors