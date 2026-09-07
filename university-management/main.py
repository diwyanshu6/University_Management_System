from models.user import User, Role

from repositories.student_repository import StudentRepository
from repositories.professor_repository import ProfessorRepository
from repositories.course_repository import CourseRepository
from repositories.enrollment_repository import EnrollmentRepository

from services.student_service import StudentService
from services.professor_service import ProfessorService
from services.course_service import CourseService
from services.enrollment_service import EnrollmentService












def print_students(students):

    print("\n===== STUDENTS =====")

    if not students:
        print("No students found.")
        return

    for student in students:

        student.display_info()
        print("----------------")


def print_professors(professors):

    print("\n===== PROFESSORS =====")

    if not professors:
        print("No professors found.")
        return

    for professor in professors:

        professor.display_info()
        print("----------------")


def print_courses(courses):

    print("\n===== COURSES =====")

    if not courses:
        print("No courses found.")
        return

    for course in courses:

        course.display_info()
        print("----------------")


def main():

 
    # USERS


    admin = User(
        "admin",
        Role.ADMIN 
    )
   
    professor_user = User(
        "professor",
        Role.PROFESSOR     
    )

    student_user = User(
        "student",
        Role.STUDENT
    )


  
    # REPOSITORIES
   

    student_repository = StudentRepository()

    professor_repository = ProfessorRepository()

    course_repository = CourseRepository()

    enrollment_repository = EnrollmentRepository()


   
    # SERVICES
   

    student_service = StudentService(
        student_repository
    )

    professor_service = ProfessorService(
        professor_repository
    )

    course_service = CourseService(
        course_repository
    )

    enrollment_service = EnrollmentService(
        enrollment_repository
    )


    
    # LOGIN
   

    print("\n==============================")
    print(" UNIVERSITY MANAGEMENT SYSTEM")
    print("==============================")

    print("\nSelect Role:")

    print("1. Admin")
    print("2. Professor")
    print("3. Student")

    role_choice = input(
        "\nEnter choice: "
    )


    if role_choice == "1":

        current_user = admin

    elif role_choice == "2":

        current_user = professor_user

    elif role_choice == "3":

        current_user = student_user

    else:

        print("Invalid role.")

        return


    print(
        f"\nLogged in as: "
        f"{current_user.role.value}"
    )


    while True:

        print("\n==============================")
        print(" MENU")
        print("==============================")

        if current_user.role == Role.ADMIN:

            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Add Professor")
            print("5. View Professors")
            print("6. Add Course")
            print("7. View Courses")
            print("8. Exit")


        elif current_user.role == Role.PROFESSOR:

            print("1. View Students")
            print("2. View Courses")
            print("3. Assign Grade")
            print("4. Exit")


        elif current_user.role == Role.STUDENT:

            print("1. View Students")
            print("2. View Courses")
            print("3. Enroll in Course")
            print("4. Exit")


        choice = input(
            "\nEnter choice: "
        )


        try:


            # ADMIN


            if current_user.role == Role.ADMIN:

                if choice == "1":

                    name = input("Student name: ")
                    email = input("Student email: ")

                    department_id = int(
                        input("Department ID: ")
                    )

                    student = student_service.add_student(
                        current_user,
                        name,
                        email,
                        department_id
                    )

                    print(
                        f"Student created with ID "
                        f"{student.student_id}"
                    )


                elif choice == "2":

                    students = student_service.get_all_students(
                        current_user
                    )

                    print_students(students)


                elif choice == "3":

                    student_id = int(
                        input("Student ID: ")
                    )

                    deleted = student_service.delete_student(
                        current_user,
                        student_id
                    )

                    if deleted:
                        print("Student deleted.")
                    else:
                        print("Student not found.")


                elif choice == "4":

                    name = input("Professor name: ")
                    email = input("Professor email: ")
                    specialization = input(
                        "Specialization: "
                    )

                    department_id = int(
                        input("Department ID: ")
                    )

                    professor = professor_service.add_professor(
                        current_user,
                        name,
                        email,
                        specialization,
                        department_id
                    )

                    print(
                        f"Professor created with ID "
                        f"{professor.professor_id}"
                    )


                elif choice == "5":

                    professors = professor_service.get_all_professors(
                        current_user
                    )

                    print_professors(professors)


                elif choice == "6":

                    course_name = input(
                        "Course name: "
                    )

                    professor_id = int(
                        input("Professor ID: ")
                    )

                    department_id = int(
                        input("Department ID: ")
                    )

                    course = course_service.add_course(
                        current_user,
                        course_name,
                        professor_id,
                        department_id
                    )

                    print(
                        f"Course created with ID "
                        f"{course.course_id}"
                    )


                elif choice == "7":

                    courses = course_service.get_all_courses(
                        current_user
                    )

                    print_courses(courses)


                elif choice == "8":

                    print("Goodbye!")

                    break


                else:

                    print("Invalid choice.")


        
            # PROFESSOR
            

            elif current_user.role == Role.PROFESSOR:

                if choice == "1":

                    students = student_service.get_all_students(
                        current_user
                    )

                    print_students(students)


                elif choice == "2":

                    courses = course_service.get_all_courses(
                        current_user
                    )

                    print_courses(courses)


                elif choice == "3":

                    enrollment_id = int(
                        input("Enrollment ID: ")
                    )

                    grade = input(
                        "Grade: "
                    ).upper()

                    enrollment_service.assign_grade(
                        current_user,
                        enrollment_id,
                        grade
                    )

                    print("Grade assigned.")


                elif choice == "4":

                    print("Goodbye!")

                    break


                else:

                    print("Invalid choice.")


           
            # STUDENT
            

            elif current_user.role == Role.STUDENT:

                if choice == "1":

                    students = student_service.get_all_students(
                        current_user
                    )

                    print_students(students)


                elif choice == "2":

                    courses = course_service.get_all_courses(
                        current_user
                    )

                    print_courses(courses)


                elif choice == "3":

                    student_id = int(
                        input("Student ID: ")
                    )

                    course_id = int(
                        input("Course ID: ")
                    )

                    enrollment = enrollment_service.enroll_student(
                        current_user,
                        student_id,
                        course_id
                    )

                    print(
                        f"Enrollment successful. "
                        f"ID: {enrollment.enrollment_id}"
                    )


                elif choice == "4":

                    print("Goodbye!")

                    break


                else:

                    print("Invalid choice.")


        except Exception as error:

            print(
                f"\nError: {error}"
            )


if __name__ == "__main__":
    main()