import json
from operator import index 



print ("Welcome in TODO list app")
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks() 

def show_menu():
    print("\n" + "=" * 30)
    print("\nMenu:")
    print ("=" * 30)
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Edit Priority")
    print("6. Mark Task as Complete")
    print("7. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    priority = input("Enter the priority (high/medium/low): ")
    tasks.append({"task": task, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['task']} - priority: {task.get('priority', 'low')} - {status}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    for task in tasks:
        print(f"{tasks.index(task) + 1}. {task['task']}")

    try:
        task_number = int(input("Enter task number to delete: "))

        if 0 < task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    for task in tasks:
        print(f"ID:{task['id']}. {task['task']} - priority: {task.get('priority', 'low')}")                    
    
    try:
        task_id = int(input("Enter task ID: "))
        for task in tasks:
            if task["id"] == task_id:
                new_task = input("Enter the new task: ")
                task["task"] = new_task
                save_tasks(tasks)
                print("Task edited successfully!")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def edit_priority(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    for task in tasks:
        print(f"ID:{task['id']}. {task['task']} - priority: {task.get('priority', 'low')}")                    
    
    try:
        task_id = int(input("Enter task ID: "))
        for task in tasks:
            if task["id"] == task_id:
                new_priority = input("Enter the new priority (high/medium/low): ")
                task["priority"] = new_priority
                save_tasks(tasks)
                print("Priority edited successfully!")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")
            
def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return
    
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{tasks.index(task) + 1}. {task['task']} - priority: {task.get('priority', 'low')} - {status}")

    try:
        task_number = int(input("Enter task number to mark as complete: "))
        
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_number - 1]['task']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def exit_app():
    print("Exiting the app. Goodbye!")

while True:
    show_menu()
 
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        show_tasks(tasks)
    elif choice == '3':
        delete_task(tasks)
    elif choice == '4':
        edit_task(tasks)
    elif choice == '5':
        edit_priority(tasks)
    elif choice == '6':
        mark_complete(tasks)
    elif choice == '7': 
        exit_app()
        break
    else:
        print("Invalid choice. Please try again.")
