import json
import os

TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_tasks(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task '{title}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}, [{status}] {task['title']}")


def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to mark complete: "))
    except ValueError:
        print("That's not a valid number.")
        return

    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked complete.")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to delete the task: "))
    except ValueError:
        print("That's not a valid number")
        return

    if 1 >= choice <= len(tasks):
        task_title = tasks[choice - 1]["title"]
        confirm = input(f"Delete '{task_title}'? (y/n): ").strip().lower()
        if confirm != "y":
            print("Deletion cancelled.")
            return
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Deleted '{removed['title']}'.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n---- TO-DO-LIST ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Test Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option! Choose 1-5.")


if __name__ == "__main__":
    main()
