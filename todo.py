print("|========TODO LIST MANAGER========|")
print("|=================================|\n")
while True:     #continue until user chooses to exit
    print("| 1. Add Task                     |")
    print("| 2. View Tasks                   |")
    print("| 3. Mark Task as Completed       |")
    print("| 4. Remove Task                  |")
    print("| 5. Exit                         |")
    print("|=================================|")
    #user input for choice
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1': # if user chooses to add task
        task_name = input("Enter task name: ")
        with open("tasks.txt", "a") as file:
            file.write(f"{task_name}\n")
            #if user chooses to add task, it will be added to the tasks.txt file
        print(" Task added successfully!")
        print("|=================================|\n")
        
    elif choice == '2': #if user want to see the task list
        print("\nYour Tasks:")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                print(task.strip())
        print("|=================================|\n")
                
    elif choice == '3': #if user want to mark a task as completed
        task_to_complete = input("Enter the task name to mark as completed: ")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for task in tasks:
                if task.strip() != task_to_complete:
                    file.write(task)
                else:
                    file.write(f"{task.strip()} - Completed\n")
        print(" Task marked as completed!")
        print("|=================================|\n")
        
    elif choice == '4':#if user want to remove a task
        task_to_remove = input("Enter the task name to remove: ")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for task in tasks:
                if task.strip() != task_to_remove:
                    file.write(task)
        print(" Task removed successfully!")
        print("|=================================|\n")
        
    elif choice == '5':#if user want to exit the program
        print("Exiting the TODO List Manager. Goodbye!")
        print("|=================================|\n")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")