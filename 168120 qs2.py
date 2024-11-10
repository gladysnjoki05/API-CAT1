class Student:
    next_id = 1  

    def __init__(self, name):
        self.name = name
        self.student_id = Student.next_id
        Student.next_id += 1  
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade {grade} added for {self.name}")

    def display_grades(self):
        if self.assignments:
            print(f"{self.name}'s Grades:")
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments recorded.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found in the course.")

    def display_all_students_grades(self):
        if self.students:
            print(f"All students and their grades for the course '{self.course_name}':")
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in the course.")


def main():
    instructor = Instructor("Sir A. Majawa", "Python Programming 101")

    while True:
        print("\n\t\t\t\tWelcome to the Course Management System.\nEnter the desired option number below.")
        print("1. Add a student to the course")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_name = input("Enter the student's name: ")
            student = Student(student_name)
            instructor.add_student(student)

        elif choice == '2':
            try:
                student_id = int(input("Enter the student's ID: "))
                assignment_name = input("Enter the assignment name: ")
                grade = float(input("Enter the grade: "))
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid input. Ensure the ID is a number and the grade is a numeric value.")

        elif choice == '3':
            instructor.display_all_students_grades()

        elif choice == '4':
            print("\n\t\t\t\tExiting the course management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
