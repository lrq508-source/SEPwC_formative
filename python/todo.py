"""A simple command-line to-do list application."""
import argparse

TASK_FILE = ".tasks.txt"


def add_task(task):
    """Add a new task to the task file.

    Input - a task to add to the list
    Return - nothing
    """
    task_file = open(TASK_FILE, "a")
    task_file.write(task + "\n")
    task_file.close()


def list_tasks():
    """List all tasks from the task file."""
    task_file = open(TASK_FILE, "r")
    tasks = task_file.read().splitlines()
    task_file.close()

    result = ""
    number = 1
    for task in tasks:
        result = result + str(number) + ". " + task + "\n"
        number = number + 1

    result = result.strip()
    return result


def remove_task(index):
    """Remove a task by its number from the task file."""
    task_file = open(TASK_FILE, "r")
    tasks = task_file.read().splitlines()
    task_file.close()

    position = index - 1

    if position >= 0 and position < len(tasks):
        tasks.pop(position)

    task_file = open(TASK_FILE, "w")
    for task in tasks:
        task_file.write(task + "\n")
    task_file.close()


def main():
    """Run the command-line todo app."""
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    