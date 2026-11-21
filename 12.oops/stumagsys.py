class Student:

    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class StudentManagement:

    def __init__(self):
        self.students = []

    def add_student(self):
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        student = Student(roll, name, course)
        self.students.append(student)

        print("Student added successfully!")

    def display_students(self):
        if len(self.students) == 0:
            print("No student records found")
        else:
            for student in self.students:
                print("\nRoll Number:", student.roll_no)
                print("Name:", student.name)
                print("Course:", student.course)

    def search_student(self):
        roll = int(input("Enter Roll Number to search: "))

        for student in self.students:
            if student.roll_no == roll:
                print("Student Found!")
                print("Name:", student.name)
                print("Course:", student.course)
                return

        print("Student not found")


obj = StudentManagement()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.display_students()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")