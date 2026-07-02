from storage import load_tasks
from tasks import (
    add_task, display_tasks, edit_priority, edit_task, filter_tasks, show_filter_menu, show_sort_menu, show_tasks, delete_task, mark_complete, sort_tasks_by_id, search_tasks, sort_tasks_by_priority
)

tasks = load_tasks()

def show_menu():
    print("="*40)
    print("           TODO APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. Show Tasks (Filter)")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Edit Priority")
    print("6. Mark Task as Complete")
    print("7. Sort Tasks Menu")
    print("8. Search Tasks")
    print("9. Exit")
    print("="*40)

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        filter_type = show_filter_menu()

        if filter_type is None:
            print("Returning to main menu.")
            continue

        filtered = filter_tasks(tasks, filter_type)
        if filtered:
            display_tasks(filtered)
        else:
            print("No tasks found for the selected filter.")
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        edit_task(tasks)
    elif choice == "5":
        edit_priority(tasks)
    elif choice == "6":
        mark_complete(tasks)
    elif choice == "7":
         sort_type = show_sort_menu()

         if sort_type is None:
            print("Returning to main menu.")
            continue

         if sort_type == "id":
            sorted_tasks = sort_tasks_by_id(tasks)
            display_tasks(sorted_tasks)

         elif sort_type == "priority":
              sorted_tasks = sort_tasks_by_priority(tasks)
              display_tasks(sorted_tasks)

    elif choice == "8":
        query = input("Enter search query: ")
        results = search_tasks(tasks, query)
        if results:
            display_tasks(results)
        else:
            print("No tasks found.")
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")