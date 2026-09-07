from database.db import Database
from models.student import Student


class StudentRepository:

    def save(self, student):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO students
            (name, email, department_id)
            VALUES (%s, %s, %s)
        """




        values = (
            student.name,
            student.email,
            student.department_id
        )

        cursor.execute(query, values)

        connection.commit()

        student.student_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return student

    def find_by_id(self, student_id):

        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT student_id, name, email, department_id
            FROM students
            WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row is None:
            return None

        return Student(
            name=row["name"],
            email=row["email"],
            student_id=row["student_id"],
            department_id=row["department_id"]
        )

    def find_all(self):

        connection = Database.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT student_id, name, email, department_id
            FROM students
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        students = []

        for row in rows:

            student = Student(
                name=row["name"],
                email=row["email"],
                student_id=row["student_id"],
                department_id=row["department_id"]
            )

            students.append(student)

        return students

    def delete(self, student_id):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM students
            WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))

        connection.commit()

        deleted = cursor.rowcount > 0

        cursor.close()
        connection.close()

        return deleted