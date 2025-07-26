from logic.note_manager import add_note, view_notes, delete_note
from logic.task_manager import add_task, view_tasks, delete_task
from logic.utils.clear_terminal import clear_terminal
import sys


def main():
    clear_terminal()
    commands = {
        "add task": add_task,
        "add note": add_note,
        "view task": view_tasks,
        "view note": view_notes,
        "delete task": delete_task,
        "delete note": delete_note,
        "exit": ""
    }

    while True:
        print("Welcome to TaskPilot\n")
        print("What do you want to do?")
        for key in commands:
            print(f" - {key}")

        todo = input("\n>>> ").strip().lower()

        if todo in commands and todo != "exit":
            commands[todo]()
        elif todo == "exit":
            sys.exit(1)
        else:
            print("Invalid command\n")



if __name__ == "__main__":
    main()