# Global lists to store student records
students = []

# Function to add a new student
def add_student():
    print("\nEnter student details:")
    sid = input("Student ID: ")
    name = input("Name: ")
    grade_level = input("Grade Level: ")
    subject = input("Subject: ")
    grade = float(input("Grade: "))

    students.append({
        'Student ID': sid,
        'Name': name,
        'Grade Level': grade_level,
        'Subject': subject,
        'Grade': grade
    })
    print(f"Student {name} added successfully!")

# Function to view all students
def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        print("-------------------------------------------------")
        print("{:<15} {:<20} {:<15} {:<20} {:<10}".format('Student ID', 'Name', 'Grade Level', 'Subject', 'Grade'))
        print("-------------------------------------------------")
        for student in students:
            print("{:<15} {:<20} {:<15} {:<20} {:<10}".format(student['Student ID'], student['Name'], 
                                                               student['Grade Level'], student['Subject'], 
                                                               student['Grade']))
        print("-------------------------------------------------")

# Function to update student record
def update_student():
    sid = input("Enter Student ID to update: ")
    found = False
    for student in students:
        if student['Student ID'] == sid:
            print("\nEnter new details (leave blank to keep current):")
            name = input(f"Name ({student['Name']}): ").strip() or student['Name']
            grade_level = input(f"Grade Level ({student['Grade Level']}): ").strip() or student['Grade Level']
            subject = input(f"Subject ({student['Subject']}): ").strip() or student['Subject']
            grade = float(input(f"Grade ({student['Grade']}): ").strip() or student['Grade'])

            student['Name'] = name
            student['Grade Level'] = grade_level
            student['Subject'] = subject
            student['Grade'] = grade
            print(f"Student {sid} updated successfully!")
            found = True
            break

    if not found:
        print(f"Student with ID {sid} not found.")

# Function to delete a student record
def delete_student():
    sid = input("Enter Student ID to delete: ")
    found = False
    for student in students:
        if student['Student ID'] == sid:
            students.remove(student)
            print(f"Student {sid} deleted successfully!")
            found = True
            break

    if not found:
        print(f"Student with ID {sid} not found.")

# Function to calculate average grade for a student
def calculate_average_grade():
    sid = input("Enter Student ID to calculate average grade: ")
    found = False
    for student in students:
        if student['Student ID'] == sid:
            print(f"\nAverage Grade for {student['Name']} ({student['Student ID']}): {student['Grade']}")
            found = True
            break
    
    if not found:
        print(f"Student with ID {sid} not found.")

# Function for user login
def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "1234":
            print("\nLogin successful!")
            return True
        else:
            print("Invalid credentials. Please try again.")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    print("Login failed. Exiting...")
    return False

# Main program loop
if __name__ == "__main__":
    if login():
        while True:
            print("\nStudent Grades Manager Menu:")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Calculate Average Grade")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                add_student()
            elif choice == '2':
                view_students()
            elif choice == '3':
                update_student()
            elif choice == '4':
                delete_student()
            elif choice == '5':
                calculate_average_grade()
            elif choice == '6':
                print("Exiting Student Grades Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    else:
        print("Program terminated.")
