undo_stack = [""]
redo_stack = []


def make_change(new_text):
    undo_stack.append(new_text)
    redo_stack.clear()
    print("Change made successfully")


def undo():
    if len(undo_stack) > 1:
        redo_stack.append(undo_stack.pop())
        print("Undo successful")
    else:
        print("Nothing to undo")


def redo():
    if redo_stack:
        undo_stack.append(redo_stack.pop())
        print("Redo successful")
    else:
        print("Nothing to redo")


def display():
    print("Current Document:", undo_stack[-1])


while True:
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        text = input("Enter new document state: ")
        make_change(text)
    elif ch == 2:
        undo()
    elif ch == 3:
        redo()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
