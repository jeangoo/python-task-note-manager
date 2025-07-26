import json
from logic.utils.date_functions import know_date, date_validator, is_future_date
from logic.utils.clear_terminal import clear_terminal


def add_note():
    clear_terminal()
    print("Enter the title of the note")
    title = input(">>> ").lower()
    print("Enter the description")
    desc = input(">>> ")
    print("Due date (D/H/Y)")
    due_date = input(">>> ")

    if not title or not desc or not due_date:
        print("Error: there are empty inputs\n")
        return
    
    if not date_validator(due_date):
        print("Error: invalid date format (must be DD/MM/YYYY)\n")
        return
    
    if not is_future_date(due_date):
        print("Error: The due date cannot be in the past.\n")
        return
    
    data = {"title": title,
            "description": desc,
            "date": know_date(),
            "due date": due_date
            }
    try:
        with open("data/notes.json", "r") as file:
            notes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        notes = []


    notes.append(data)

    with open("data/notes.json", "w") as file:
        json.dump(notes, file, indent=4)



def view_notes():
    note = input("Note to search (title): ").lower()

    try: 
        with open("data/notes.json", "r") as file:
            data = json.load(file)
 
        for item in data:
            if item["title"] == note:
                print(f"\nTitle: {item["title"]}")
                print(f"Description: {item["description"]}")
                print(f"Date: {item["date"]}")
                print(f"Due date: {item["due date"]}\n")
                break
        else:
            print("\nNote not found\n")

    except FileNotFoundError:
        print("The note files does not exist.\n")
    except json.JSONDecodeError:
         print("The notes file is corrupted or empty.\n")

def delete_note():
    title_delete = input("Note to delete (title): ").lower()

    try: 
        with open("data/notes.json", "r") as file:
            data = json.load(file)

        for i, item in enumerate(data):
            if item["title"] == title_delete:
                del data[i]
                with open("data/notes.json", "w") as file:
                    json.dump(data, file, indent=4)
                print("\nNote deleted successfully.\n")
                break
        else:
            print("\nNote not found\n")


    except FileNotFoundError:
        print("The note files does not exist.\n")
    except json.JSONDecodeError:
         print("The notes file is corrupted or empty.\n")


