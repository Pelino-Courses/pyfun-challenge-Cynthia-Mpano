from student import Student
from instructor import Instructor
from course import Course
from teaching_assistant import TeachingAssistant

# Store students and courses
students = []
courses = []

# Function to create a student
def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_id = input("Enter student ID: ")
    student = Student(name, age, student_id)
    students.append(student)
    print(f"Student {student.name} added successfully!\n")

# Function to create a course
def create_course():
    title = input("Enter course title: ")
    course_code = input("Enter course code: ")
    credits = int(input("Enter course credits: "))
    course = Course(title, course_code, credits)
    courses.append(course)
    print(f"Course {course.title} added successfully!\n")

# Function to enroll a student in a course
def enroll_student():
    if not students or not courses:
        print("No students or courses available for enrollment!\n")
        return

    print("Available Students:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student.name} (ID: {student.student_id})")

    student_index = int(input("Select student by number: ")) - 1
    if student_index not in range(len(students)):
        print("Invalid selection!\n")
        return

    print("\nAvailable Courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course.title} ({course.course_code})")

    course_index = int(input("Select course by number: ")) - 1
    if course_index not in range(len(courses)):
        print("Invalid selection!\n")
        return

    selected_student = students[student_index]
    selected_course = courses[course_index]
    selected_course.enroll_student(selected_student)
    print(f"{selected_student.name} has been enrolled in {selected_course.title}!\n")

# Main loop
while True:
    print("\nUniversity Enrollment System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. View Enrolled Students")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        create_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        if not courses:
            print("No courses available to view enrollment!\n")
        else:
            for course in courses:
                print(f"\nStudents enrolled in {course.title}:")
                for student in course:
                    print(f"- {student.name}")
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option! Please try again.\n")