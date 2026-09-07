CREATE DATABASE IF NOT EXISTS university_db;

USE university_db;


CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE SET NULL
);


CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    specialization VARCHAR(100),
    department_id INT,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE SET NULL
);


CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    professor_id INT,
    department_id INT,

    FOREIGN KEY (professor_id)
        REFERENCES professors(professor_id)
        ON DELETE SET NULL,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE SET NULL
);


CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade VARCHAR(5),

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE,

    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
        ON DELETE CASCADE,

    UNIQUE(student_id, course_id)
);