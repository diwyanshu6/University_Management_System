from database.db import Database
from models.enrollment import Enrollment


class EnrollmentRepository:

    def save(self, enrollment):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO enrollments
            (student_id, course_id, grade)
            VALUES (%s, %s, %s)
        """

        values = (
            enrollment.student_id,
            enrollment.course_id,
            enrollment.grade
        )

        cursor.execute(query, values)

        connection.commit()

        enrollment.enrollment_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return enrollment


    def assign_grade(
        self,
        enrollment_id,
        grade
    ):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE enrollments
            SET grade = %s
            WHERE enrollment_id = %s
        """

        cursor.execute(
            query,
            (grade, enrollment_id)
        )

        connection.commit()

        updated = cursor.rowcount > 0

        cursor.close()
        connection.close()

        return updated


    def find_all(self):

        connection = Database.get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        query = """
            SELECT
                enrollment_id,
                student_id,
                course_id,
                grade
            FROM enrollments
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        enrollments = []

        for row in rows:

            enrollment = Enrollment(
                student_id=row["student_id"],
                course_id=row["course_id"],
                grade=row["grade"],
                enrollment_id=row["enrollment_id"]
            )

            enrollments.append(enrollment)

        return enrollments