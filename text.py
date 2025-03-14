import os

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return file.readlines()



def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        file.writelines(notes)



def add_note():
    note = input("Enter your note: ") + "\n"
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added successfully!")



def view_notes():

    notes = load_notes()
    if not notes:
        print("No notes available.")
    else:
        print("\nYour Notes:")
        for index, note in enumerate(notes, 1):
            print(f"{index}. {note.strip()}")



def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes to delete.")
        return


    view_notes()
    try:
        index = int(input("Enter note number to delete: ")) - 1
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            save_notes(notes)
            print(f"Deleted note: {deleted_note.strip()}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\nNote-Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
