from database.db import Database
from models.course import Course


class CourseRepository:

    def save(self, course):

        connection = Database.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO courses
            (course_name, professor_id, department_id)
            VALUES (%s, %s, %s)
        """

        values = (
            course.course_name,
            course.professor_id,
            course.department_id
        )

        cursor.execute(query, values)

        connection.commit()

        course.course_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return course


    def find_all(self):

        connection = Database.get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        query = """
            SELECT *
            FROM courses
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        courses = []

        for row in rows:

            courses.append(
                Course(
                    course_name=row["course_name"],
                    course_id=row["course_id"],
                    professor_id=row["professor_id"],
                    department_id=row["department_id"]
                )
            )

        return courses