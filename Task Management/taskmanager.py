from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,task_descriptions):
        for task_description in task_descriptions.split(";"):
            task = Task(task_description.strip())
            self.tasks.append(task)
            print(f"{task} added to tasks!")

    def view_tasks(self):
        print("TASKS")
        print("--------")
        for task in self.tasks:
            if task.completed:
                print(f"~~{task}~~")
            else:
                print(task)
    
    def mark_as_complete(self,task_descriptions):
        for task in self.tasks:
            if task.task_details == task_descriptions:
                task.completed = True

    def delete_tasks(self,task_descriptions):
        for task in self.tasks:
            if task.task_details == task_descriptions:
                self.tasks.remove(task)
                print(f"{task} deleted successfully!")
    
    

def main():
    system = TaskManager()

    while True:
        print("\n Task Management System")
        print("1. ADD TASK(s)")
        print("2. VIEW TASKS")
        print("3. MARK AS COMPLETE")
        print("4. DELETE TASK(s)")
        print("5. EXIT")
    
        choice = input("Enter your choice:")

        if choice == '1':
            task_descriptions = input("Input Task(s) separated by a semicolon(;): ")
            system.add_task(task_descriptions)

        elif choice == '2':
            system.view_tasks()

        elif choice == '3':
            task_descriptions = input("Enter Task you want to mark as complete:")
            system.mark_as_complete(task_descriptions)
            system.view_tasks()

        elif choice == '4':
            task_descriptions = input("Enter Task to delete:")
            system.delete_tasks(task_descriptions)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid input!Try Again")

if __name__ == "__main__":
    main()