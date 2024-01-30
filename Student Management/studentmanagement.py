from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self,name,age,grade):
        student = Student(name,age,grade)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_students(self):
        for student in self.students:
            print(student)
        
    def upgrade_student_grade(self,name,new_grade):
        for student in self.students:
            if student.name == name:
                student.grade = new_grade
                print(f"Grade updated for {name}")

    def delete_students(self,name):
        for student in self.students:
            if name == student.name:
                self.students.remove(student)
                print(f"Successfully deleted Student {name}")

def main():
    system = StudentManagementSystem()

    while True:
        print("\n Student Management System")
        print("1. ADD STUDENTS")
        print("2. DISPLAY STUDENTS")
        print("3. UPDATE STUDENTS GRADE")
        print("4. DELETE STUDENTS")
        print("5. EXIT")

        choice = input("Enter your choice:")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            system.add_students(name,age,grade)
        
        elif choice == '2':
            system.display_students()

        elif choice == '3':
            name = input("Enter student name to update grade: ")
            new_grade = input("Enter new grade: ")
            system.upgrade_student_grade(name,new_grade)
        
        elif choice == '4':
            name = input("Enter student name to delete: ")
            system.delete_students(name)
        
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice.Please try again")

if __name__ == "__main__":
    main()
        