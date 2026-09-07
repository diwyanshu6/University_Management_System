# University Management System

A Python-based University Management System designed using **Object-Oriented Programming (OOP)** and a **layered architecture**.

The project demonstrates:

* OOP principles
* SOLID principles
* Repository Pattern
* Service Layer
* Dependency Injection
* Role-Based Authorization
* Database CRUD operations
* Many-to-Many relationships
* Exception Handling

---

# 1. Project Overview

The University Management System manages:

* Students
* Professors
* Courses
* Enrollments
* Users and Roles
* Permissions

The application has three types of users:

```text
Admin
Professor
Student
```

Each role has different operations and permissions.

---

# 2. Application Startup

The application starts from:

```text
main.py
```

Run the application using:

```bash
python main.py
```

The first screen is:

```text
==============================
 UNIVERSITY MANAGEMENT SYSTEM
==============================

Select Role:

1. Admin
2. Professor
3. Student

Enter choice:
```

The selected role becomes the current user.

---

# 3. User Roles

## 3.1 Admin

When the user selects:

```text
1. Admin
```

the application shows:

```text
==============================
 MENU
==============================

1. Add Student
2. View Students
3. Delete Student
4. Add Professor
5. View Professors
6. Add Course
7. View Courses
8. Exit
```

### Admin Responsibilities

The Admin can:

* Add students
* View students
* Delete students
* Add professors
* View professors
* Add courses
* View courses

---

## 3.2 Professor

When the user selects:

```text
2. Professor
```

the application shows:

```text
==============================
 MENU
==============================

1. View Students
2. View Courses
3. Assign Grade
4. Exit
```

### Professor Responsibilities

The Professor can:

* View students
* View courses
* Assign grades to enrollments

---

## 3.3 Student

When the user selects:

```text
3. Student
```

the application shows:

```text
==============================
 MENU
==============================

1. View Students
2. View Courses
3. Enroll in Course
4. Exit
```

### Student Responsibilities

The Student can:

* View students
* View courses
* Enroll in a course

---

# 4. Role-Based Authorization

The application uses roles and permissions to control operations.

Roles:

```text
ADMIN
PROFESSOR
STUDENT
```

Permissions:

```text
ADD_STUDENT
DELETE_STUDENT
ADD_PROFESSOR
ADD_COURSE
ENROLL_COURSE
ASSIGN_GRADE
VIEW_DATA
```

Permissions are represented using Python's `Enum`:

```python
class Permission(Enum):

    ADD_STUDENT = "ADD_STUDENT"
    DELETE_STUDENT = "DELETE_STUDENT"
    ADD_PROFESSOR = "ADD_PROFESSOR"
    ADD_COURSE = "ADD_COURSE"
    ENROLL_COURSE = "ENROLL_COURSE"
    ASSIGN_GRADE = "ASSIGN_GRADE"
    VIEW_DATA = "VIEW_DATA"
```

Instead of using arbitrary strings such as:

```python
"ADD_STUDENT"
```

throughout the application, the system uses:

```python
Permission.ADD_STUDENT
```

This gives a centralized and fixed set of valid permissions.

---

# 5. Authorization Flow

When a user performs an operation, the service checks whether the user has the required permission.

Example:

```python
AuthorizationService.check_permission(
    user,
    Permission.ADD_STUDENT
)
```

The authorization service checks the user's permission.

If the user is authorized:

```text
Permission granted
       ↓
Continue execution
```

If the user is not authorized:

```text
Permission denied
       ↓
raise PermissionError
       ↓
Stop operation
```

The error is eventually handled by `main.py`.

---

# 6. Project Structure

```text
University_management/
│
├── main.py
│
├── models/
│   ├── person.py
│   ├── student.py
│   ├── professor.py
│   ├── course.py
│   ├── enrollment.py
│   └── user.py
│
├── repositories/
│   ├── student_repository.py
│   ├── professor_repository.py
│   ├── course_repository.py
│   └── enrollment_repository.py
│
├── services/
│   ├── student_service.py
│   ├── professor_service.py
│   ├── course_service.py
│   ├── enrollment_service.py
│   └── authorization_service.py
│
└── database/
    └── database.py
```

---

# 7. Folder Responsibilities

## `models/`

The model layer represents the entities in the university system.

Main entities:

```text
Person
Student
Professor
Course
Enrollment
User
```

The model represents **what an entity is and what data it contains**.

For example:

```python
class Student(Person):

    def __init__(
        self,
        name,
        email,
        student_id=None,
        department_id=None
    ):
        super().__init__(name, email)

        self.student_id = student_id
        self.department_id = department_id
```

The model should not be responsible for:

* SQL queries
* Database connections
* User menus
* Authorization logic

---

# 8. Person and Inheritance

`Person` is an abstract base class.

```python
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @abstractmethod
    def display_info(self):
        pass
```

`Student` and `Professor` inherit from `Person`.

```text
             Person
             /    \
            /      \
       Student    Professor
```

This represents:

```text
Student IS-A Person
Professor IS-A Person
```

---

# 9. Abstraction

`Person` is abstract because it contains:

```python
@abstractmethod
def display_info(self):
    pass
```

This means subclasses must provide their own implementation of `display_info()`.

For example:

```python
class Student(Person):

    def display_info(self):
        print("Student information")
```

and:

```python
class Professor(Person):

    def display_info(self):
        print("Professor information")
```

`Person` can contain concrete methods such as:

```python
__init__()
name
email
```

An abstract class does not need to contain only abstract methods.

---

# 10. Encapsulation and `@property`

The `Person` class stores:

```python
self._name
self._email
```

and exposes them using properties:

```python
@property
def name(self):
    return self._name
```

This allows:

```python
student.name
```

instead of:

```python
student.get_name()
```

`@property` therefore provides a getter-like interface while allowing controlled access to internal data.

---

# 11. Polymorphism

Both `Student` and `Professor` implement:

```python
display_info()
```

The same method call can produce different behavior.

```python
student.display_info()
professor.display_info()
```

The actual implementation depends on the object's type.

This is runtime polymorphism.

---

# 12. Repositories

The `repositories/` folder contains classes responsible for **database access**.

Repositories include:

```text
StudentRepository
ProfessorRepository
CourseRepository
EnrollmentRepository
```

Typical repository operations are:

```text
save()
find_by_id()
find_all()
delete()
update()
```

The repository is responsible for:

* Executing SQL
* Using database connections
* Using cursors
* Fetching database results
* Converting database rows into application objects

The repository should not contain business rules.

---

# 13. Why Use a Repository?

Without a repository, the service could directly execute SQL:

```text
Service
   ↓
SQL
   ↓
Database
```

This would tightly couple business logic with database implementation.

Instead:

```text
Service
   ↓
Repository
   ↓
Database
```

The service doesn't need to know how SQL is written.

For example:

```python
student = self.student_repository.find_by_id(student_id)
```

The service only knows that the repository can find a student.

---

# 14. Services

The `services/` folder contains business logic.

Services include:

```text
StudentService
ProfessorService
CourseService
EnrollmentService
AuthorizationService
```

The service layer is responsible for:

* Authorization
* Validation
* Business rules
* Creating model objects
* Calling repositories
* Coordinating operations

Example:

```python
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
```

The service first authorizes the operation, validates input, creates the model object, and finally delegates persistence to the repository.

---

# 15. Authorization Service

`authorization_service.py` is responsible for permission checking.

Example:

```python
AuthorizationService.check_permission(
    user,
    Permission.ADD_STUDENT
)
```

It checks whether the current user is allowed to perform the operation.

The method can be defined as a static method:

```python
@staticmethod
def check_permission(user, permission):
    ...
```

Because the method does not need an `AuthorizationService` instance.

It only needs:

```text
user
permission
```

---

# 16. Database Layer

The `database/` folder contains database connection logic.

Its responsibility is to provide a database connection to repositories.

The general flow is:

```text
Repository
    ↓
Database.get_connection()
    ↓
Connection
    ↓
Cursor
    ↓
SQL
    ↓
Database
```

The repository uses the cursor to execute SQL queries.

---

# 17. Cursor

A cursor is provided by the database driver.

It is used to:

* Execute SQL queries
* Retrieve query results

Example:

```python
cursor.execute(query, (student_id,))
```

For a `SELECT` query:

```python
student = cursor.fetchone()
```

or:

```python
students = cursor.fetchall()
```

The connection establishes communication with the database, while the cursor is used to execute statements and access their results.

---

# 18. Dependency Injection

The application uses constructor dependency injection.

Example:

```python
student_repository = StudentRepository()

student_service = StudentService(
    student_repository
)
```

The repository is created outside the service and passed into the service.

The service receives its dependency:

```python
class StudentService:

    def __init__(self, student_repository):
        self.student_repository = student_repository
```

Instead of:

```python
class StudentService:

    def __init__(self):
        self.student_repository = StudentRepository()
```

This reduces coupling.

It also makes testing easier because a mock or fake repository can be injected.

```text
Production:

StudentService
      ↓
StudentRepository
      ↓
Database
```

Testing:

```text
StudentService
      ↓
MockStudentRepository
      ↓
Fake/Test Data
```

---

# 19. Many-to-Many Student-Course Relationship

A student can enroll in multiple courses.

A course can contain multiple students.

Therefore:

```text
Student ←────────────→ Course
            M:N
```

A direct many-to-many relationship is represented using an `Enrollment` entity.

```text
Student
   │
   │ 1:N
   ↓
Enrollment
   ↑
   │ N:1
   │
Course
```

The original relationship:

```text
Student ←→ Course
```

becomes:

```text
Student → Enrollment → Course
```

---

# 20. Why Enrollment Is Needed

`Enrollment` represents a particular student-course relationship.

For example:

```text
Rahul
   ↓
Enrollment
   ↓
Python
```

The enrollment can contain information that belongs to the relationship itself:

```text
enrollment_id
student_id
course_id
semester
grade
status
enrollment_date
```

A grade does not belong directly to the Student because one student can have different grades for different courses.

For example:

```text
Rahul → Python → A
Rahul → DBMS   → B
Rahul → Java   → A+
```

The grade therefore belongs to the specific enrollment.

---

# 21. Admin Add Student — Complete Request Flow

Suppose an Admin enters:

```text
Student name: Rahul
Student email: rahul@gmail.com
Department ID: 10
```

### Step 1 — Main

`main.py` receives the input.

```python
student_service.add_student(
    current_user,
    name,
    email,
    department_id
)
```

### Step 2 — Service

`StudentService` receives the request.

```text
StudentService
```

### Step 3 — Authorization

The service checks:

```python
AuthorizationService.check_permission(
    user,
    Permission.ADD_STUDENT
)
```

### Step 4 — Validation

The service validates:

```text
Name is not empty
Email is not empty
```

### Step 5 — Model

The service creates:

```python
Student(
    name="Rahul",
    email="rahul@gmail.com",
    department_id=10
)
```

### Step 6 — Repository

The service calls:

```python
student_repository.save(student)
```

### Step 7 — Database

The repository executes SQL:

```sql
INSERT INTO students (...)
VALUES (...);
```

### Step 8 — Response

The result travels back:

```text
Database
   ↓
Repository
   ↓
Service
   ↓
main.py
   ↓
User
```

Finally:

```text
Student created with ID 1
```

---

# 22. Complete Request Pipeline

The general request pipeline is:

```text
                         USER
                           │
                           ▼
                        main.py
                           │
                           ▼
                    SERVICE LAYER
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        Authorization              Validation
              │                         │
              └────────────┬────────────┘
                           ▼
                    Business Logic
                           │
                           ▼
                  REPOSITORY LAYER
                           │
                           ▼
                       DATABASE
```

The response follows:

```text
DATABASE
   ↓
REPOSITORY
   ↓
SERVICE
   ↓
MAIN
   ↓
USER
```

---

# 23. Complete Admin Request

```text
Admin
  ↓
main.py
  ↓
StudentService
  ↓
AuthorizationService
  ↓
Validation
  ↓
Student Model
  ↓
StudentRepository
  ↓
Database
  ↓
StudentRepository
  ↓
StudentService
  ↓
main.py
  ↓
Admin
```

---

# 24. Complete Professor Request

For assigning a grade:

```text
Professor
    ↓
main.py
    ↓
EnrollmentService
    ↓
AuthorizationService
    ↓
Check ASSIGN_GRADE
    ↓
Business Validation
    ↓
EnrollmentRepository
    ↓
Database
    ↓
Update Enrollment
    ↓
EnrollmentRepository
    ↓
EnrollmentService
    ↓
main.py
    ↓
Professor
```

---

# 25. Complete Student Request

For course enrollment:

```text
Student
    ↓
main.py
    ↓
EnrollmentService
    ↓
AuthorizationService
    ↓
Check ENROLL_COURSE
    ↓
Business Validation
    ↓
Create Enrollment
    ↓
EnrollmentRepository
    ↓
Database
    ↓
Enrollment saved
    ↓
EnrollmentRepository
    ↓
EnrollmentService
    ↓
main.py
    ↓
Student
```

---

# 26. SOLID Principles

The project applies the SOLID principles to keep responsibilities separated and the system easier to maintain.

---

## S — Single Responsibility Principle

> A class should have one primary responsibility.

Examples:

```text
Student
→ Represents student data

StudentRepository
→ Handles student database operations

StudentService
→ Handles student business logic

AuthorizationService
→ Handles permission checking

Database
→ Handles database connection

main.py
→ Handles application interaction
```

Instead of one large class doing everything, responsibilities are separated.

---

# 27. O — Open/Closed Principle

> Classes should be open for extension but closed for modification.

`Person` provides a common abstraction:

```python
class Person(ABC):
    ...
```

New types can extend it:

```python
class Librarian(Person):
    ...
```

The existing `Person` implementation does not need to be modified simply because a new person type is added.

---

# 28. L — Liskov Substitution Principle

> A subclass should be usable wherever its parent type is expected.

`Student` and `Professor` are subclasses of `Person`.

```text
        Person
        /    \
       /      \
 Student    Professor
```

A function expecting a `Person` can accept either:

```python
def show_person(person):
    person.display_info()
```

Both are valid:

```python
show_person(student)
show_person(professor)
```

Because both subclasses satisfy the `Person` contract.

---

# 29. I — Interface Segregation Principle

> A class should not be forced to depend on methods it does not need.

The application separates responsibilities into focused services:

```text
StudentService
ProfessorService
CourseService
EnrollmentService
AuthorizationService
```

Instead of creating one huge service containing unrelated operations, responsibilities are divided into smaller, focused components.

---

# 30. D — Dependency Inversion Principle

> High-level modules should not be tightly coupled to low-level implementations.

`StudentService` receives its repository:

```python
class StudentService:

    def __init__(self, student_repository):
        self.student_repository = student_repository
```

`main.py` provides the dependency:

```python
student_repository = StudentRepository()

student_service = StudentService(
    student_repository
)
```

This is constructor dependency injection.

It allows the repository implementation to be replaced without changing the service's business logic.

---

# 31. Other OOP Concepts

## Abstraction

Using:

```python
ABC
abstractmethod
```

to define common behavior.

---

## Encapsulation

Using private/internal attributes:

```python
self._name
self._email
```

and properties:

```python
@property
def name(self):
    return self._name
```

---

## Inheritance

```text
Person
  ↑
Student
Professor
```

---

## Polymorphism

Different subclasses implement:

```python
display_info()
```

in their own way.

---

## Enum

`Role` and `Permission` use Enum to represent fixed sets of values.

Example:

```python
Role.ADMIN
Permission.ADD_STUDENT
```

---

## Static Method

Authorization checking can be implemented as:

```python
@staticmethod
def check_permission(user, permission):
    ...
```

because it does not require an instance of `AuthorizationService`.

---

# 32. Exception Handling

The service layer raises exceptions when something is invalid.

For example:

```python
if not name.strip():
    raise ValueError(
        "Student name cannot be empty."
    )
```

Authorization can raise:

```python
raise PermissionError(
    "Permission denied."
)
```

`main.py` catches the errors:

```python
try:
    ...
except Exception as error:
    print(f"\nError: {error}")
```

This separates:

```text
Service
→ Detect and raise the problem

main.py
→ Display the problem to the user
```

---

# 33. Separation of Concerns

The application separates different responsibilities.

```text
main.py
    ↓
User interaction

services/
    ↓
Business logic

repositories/
    ↓
Data access

models/
    ↓
Domain entities

database/
    ↓
Database connection
```

This prevents one layer from becoming responsible for everything.

---

# 34. Architecture Summary

The complete architecture can be represented as:

```text
                         USER
                           │
                           ▼
                        MAIN.PY
                           │
                           ▼
                    SERVICE LAYER
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
      Authorization    Validation    Business Rules
            │              │              │
            └──────────────┼──────────────┘
                           │
                           ▼
                  REPOSITORY LAYER
                           │
                           ▼
                    DATABASE LAYER
                           │
                           ▼
                       DATABASE
```

---

# 35. Layer Responsibilities — Quick Reference

| Layer                      | Responsibility                               |
| -------------------------- | -------------------------------------------- |
| `main.py`                  | User interaction and application flow        |
| `models/`                  | Represents application entities              |
| `services/`                | Business logic, validation and authorization |
| `repositories/`            | Database CRUD operations                     |
| `database/`                | Database connection                          |
| `authorization_service.py` | Permission checking                          |

---

# 36. Interview Explanation

A concise explanation of the project:

> I built a University Management System using Python and a layered architecture. The application has Admin, Professor, and Student roles with role-based permissions. The `main.py` handles user interaction and wires the application components together. The service layer contains business logic, validation, and authorization, while the repository layer handles database operations. Models represent entities such as Student, Professor, Course, and Enrollment. I used an Enrollment entity to resolve the many-to-many relationship between students and courses. I also used constructor dependency injection to reduce coupling and applied SOLID principles to keep the system maintainable and extensible.

---

# 37. Complete Mental Model

The most important thing to remember when explaining the project is:

```text
USER
  │
  ▼
MAIN
  │
  │ What operation does the user want?
  ▼
SERVICE
  │
  │ Is the user allowed?
  │ Is the input valid?
  │ What business rules apply?
  ▼
REPOSITORY
  │
  │ How do I access the data?
  ▼
DATABASE
  │
  │ Store / Retrieve / Update / Delete
  ▼
REPOSITORY
  │
  ▼
SERVICE
  │
  ▼
MAIN
  │
  ▼
USER
```

In one sentence:

> **Main handles interaction, Service handles decisions and business rules, Repository handles data access, Model represents the data, and Database stores the data.**
