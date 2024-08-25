import threading
import time
from datetime import datetime  # Import datetime for mark_as_completed

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found.")

def mark_as_completed(task):
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = tasks[index] + f" [Completed on {datetime.now()}]"
        print("Task marked as completed.")
    else:
        print("Task not found.")

def display_tasks(task_list, indent=0):
    """Displays tasks with proper indentation for sublists."""
    for idx, item in enumerate(task_list, start=1):
        if isinstance(item, dict):
            sublist_name, sublist_tasks = list(item.items())[0]
            print(f"{' ' * indent}{1+((idx-1)/10)}. Sublist: {sublist_name}")
            display_tasks(sublist_tasks, indent + 4)
        else:
            print(f"{' ' * indent}{idx}. {item}")

def create_sublist():
    sublist_name = input("Enter the name of the sublist: ")
    sublist_tasks = []
    while True:
        task = input("Enter task for the sublist (or 'done' to finish): ")
        if task.lower() == 'done':
            break
        sublist_tasks.append(task)
    tasks.append({sublist_name: sublist_tasks})
    print("Sublist created successfully.")

def start_timer(work_duration, break_duration):
    def work_thread():
        print(f"[TIMER] Work session started for {work_duration} minutes.")
        time.sleep(work_duration * 60)
        print(f"[TIMER] Work session ended.")
        start_break(break_duration)

    def start_break(duration):
        print(f"[TIMER] Break session started for {duration} minutes.")
        time.sleep(duration * 60)
        print(f"[TIMER] Break session ended.")
        start_work(work_duration)

    def start_work(duration):
        thread = threading.Thread(target=work_thread)
        thread.start()  # Start the work thread
        print(f"[MAIN] Work thread started with ID: {thread.ident}")
    start_work(work_duration)


while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Create Sublist")
    print("6. Start Timer")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        task = input("Enter the task to mark as completed: ")
        mark_as_completed(task)
    elif choice == "4":
        display_tasks(tasks)
    elif choice == "5":
        create_sublist()
    elif choice == "6":
        work_duration = int(input("Enter the work duration in minutes: "))
        break_duration = int(input("Enter the break duration in minutes: "))
        start_timer(work_duration, break_duration)
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")