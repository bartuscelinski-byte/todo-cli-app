from storage import save_tasks

def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    
    else: 
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"ID:{task['id']}. {task['task']} - priority: {task.get('priority', 'low')} - {status}")

def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None 

def add_task(tasks):
    task = input("Enter the task: ")
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    priority = input("Enter the priority (high/medium/low): ")
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Setting to 'low' by default.")
        priority = "low"
    tasks.append({"id": new_id, "task": task, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def show_tasks(tasks):
    display_tasks(tasks)

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    display_tasks(tasks)
    try:
        task_id = int(input("Enter task ID: "))

        task = get_task_by_id(tasks, task_id)
        if task:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")

        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    display_tasks(tasks)
    try:
        task = get_task_by_id(tasks, int(input("Enter task ID: ")))
        if task:
            new_task = input("Enter the new task: ")
            task["task"] = new_task
            save_tasks(tasks)
            print("Task edited successfully!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")

def edit_priority(tasks):
    if not tasks:
        print("No tasks to edit.")
        return
    display_tasks(tasks)
    try:
        get_task = get_task_by_id(tasks, int(input("Enter task ID: ")))
        if get_task:
            new_priority = input("Enter the new priority (high/medium/low): ")
            if new_priority not in ["high", "medium", "low"]:
                print("Invalid priority. Setting to 'low' by default.")
                new_priority = "low"
            get_task["priority"] = new_priority
            save_tasks(tasks)
            print("Task priority edited successfully!")
    except ValueError:
        print("Invalid input.")

def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    
    display_tasks(tasks)

    try:
        task_id = int(input("Enter task ID: "))

        get_task_by_ids = get_task_by_id(tasks, task_id)
        if get_task_by_ids:
            get_task_by_ids["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")

def sort_tasks_by_id(tasks):
    return sorted(tasks, key=lambda task: task["id"])

def sort_tasks_by_priority(tasks):
    priority_order = {
        "high": 3,
        "medium": 2,
        "low": 1
    }
    return sorted(tasks, key=lambda task: priority_order.get(task.get("priority", "low"), 0), reverse=True)

def show_sort_menu():
    print("\n--- SORT TASKS ---")
    print("1. Sort by ID")
    print("2. Sort by Priority")
    print("------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        return "id"
    elif choice == "2":
        return "priority"
    else:
        print("Invalid choice.")
        return None

    
def filter_tasks(tasks, filter_type):
    task_filter = []
    if filter_type == "all":
        return tasks 
    elif filter_type == "completed":
        task_filter = [task for task in tasks if task["completed"]]
    elif filter_type == "pending":
        task_filter = [task for task in tasks if not task["completed"]]
    else:
        print("Invalid filter type. Use 'all', 'completed' or 'pending'.")
        return

    return task_filter

def search_tasks(tasks, query):
    return [task for task in tasks if query.lower() in task["task"].lower()]

def show_filter_menu():
    print("\nFilter Tasks")
    print("1. View all tasks")
    print("2. View completed tasks")
    print("3. View pending tasks")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        return "all"
    if choice == "2":
        return "completed"
    if choice == "3":
        return "pending"
    else:
        print("Invalid choice.")
        return None 
    
    