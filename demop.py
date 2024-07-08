class Student:
    def __init__(self, name, roll_number, age, contact):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.contact = contact

class StudentProgram:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, age, contact):
        student = Student(name, roll_number, age, contact)
        self.students.append(student)

    def display_student_details(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll_number}")
                print(f"Age: {student.age}")
                print(f"Contact: {student.contact}")
                break
        else:
            print("Student not found.")

    def update_student_details(self, roll_number, name, age, contact):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = name
                student.age = age
                student.contact = contact
                print("Student details updated.")
                break
        else:
            print("Student not found.")

# Example usage:
program = StudentProgram()
program.add_student("Alice", 101, 20, "alice@example.com")
program.add_student("Bob", 102, 22, "bob@example.com")

# Display student details
program.display_student_details(101)

# Update student details
program.update_student_details(102, "Bobby", 23, "bobby@example.com")
program.display_student_details(102)
