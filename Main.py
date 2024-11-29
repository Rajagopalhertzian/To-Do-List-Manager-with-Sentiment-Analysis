from task_manager import add_task, delete_task, display_tasks, load_tasks_from_csv

def main():
    print("Welcome to the To-Do List Manager!")
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Load Tasks from CSV")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description (optional): ")
            add_task(name, description)
        elif choice == "2":
            name = input("Enter task name to delete: ")
            delete_task(name)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            file_path = input("Enter the CSV file path: ")
            load_tasks_from_csv(file_path)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
