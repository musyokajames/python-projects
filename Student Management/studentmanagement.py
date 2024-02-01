from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self,name,age,grade):
        student = Student(name,age,grade)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_students(self):
        print("Name:Age:Grade")
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

def save_students_to_file(students,filename = "student_data.txt"):
        try:
            with open (filename ,"w") as file:
                for student in students:
                    file.write(student.__str__())
                print(f"Student successfully added to {filename}")
        except Exception as e:
            print(f"Unable to save contact to {filename}.Reason:{e}")


def load_students_from_file(filename="student_data.txt"):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, age, grade = line.strip().split(":")
                student = Student(name, age, grade)
                students.append(student)
        print(f"Student data successfully loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    except Exception as e:
        print(f"Unable to load student data from {filename}. Reason: {e}")
    return students
            

def main():
    system = StudentManagementSystem()
    system.students = load_students_from_file()

    while True:
        print("\n Student Management System")
        print("1. ADD STUDENTS")
        print("2. DISPLAY STUDENTS")
        print("3. UPDATE STUDENTS GRADE")
        print("4. DELETE STUDENTS")
        print("5. EXIT")

        choice = input("Enter your choice:")

        if choice == '1':
            name = input("Enter name: ").upper()
            age = input("Enter age: ")
            grade = input("Enter grade: ").upper()
            system.add_students(name,age,grade)
        
        elif choice == '2':
            system.display_students()

        elif choice == '3':
            name = input("Enter student name to update grade: ").upper()
            new_grade = input("Enter new grade: ").upper()
            system.upgrade_student_grade(name,new_grade)
        
        elif choice == '4':
            name = input("Enter student name to delete: ").upper()
            system.delete_students(name)
        
        elif choice == '5':
            print("Exiting...")
            save_students_to_file(system.students)
            break

        else:
            print("Invalid choice.Please try again")

            

if __name__ == "__main__":
    main()
        