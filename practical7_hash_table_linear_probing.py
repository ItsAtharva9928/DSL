SIZE = 10
DELETED = -1
table = [None] * SIZE


def insert(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None or table[pos] == DELETED:
            table[pos] = key
            print("Inserted at index", pos)
            return

        if table[pos] == key:
            print("Key already exists")
            return

    print("Hash Table is Full")


def search(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            break

        if table[pos] == key:
            print("Key found at index", pos)
            return

    print("Key not found")


def delete(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            break

        if table[pos] == key:
            table[pos] = DELETED
            print("Deleted from index", pos)
            return

    print("Key not found")


def display():
    for i in range(SIZE):
        if table[i] is None:
            print(i, ":", "Empty")
        elif table[i] == DELETED:
            print(i, ":", "Deleted")
        else:
            print(i, ":", table[i])


while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        insert(key)
    elif ch == 2:
        key = int(input("Enter key: "))
        search(key)
    elif ch == 3:
        key = int(input("Enter key: "))
        delete(key)
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
