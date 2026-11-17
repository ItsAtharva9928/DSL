class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Record Added")

    def delete(self, roll):
        temp = self.head
        prev = None

        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                print("Record Deleted")
                return
            prev = temp
            temp = temp.next

        print("Record Not Found")

    def update(self, roll, name, marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = name
                temp.marks = marks
                print("Record Updated")
                return
            temp = temp.next
        print("Record Not Found")

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(temp.roll, temp.name, temp.marks)
                return
            temp = temp.next
        print("Record Not Found")

    def display(self):
        temp = self.head
        if temp is None:
            print("No Records")
            return
        while temp:
            print(temp.roll, temp.name, temp.marks)
            temp = temp.next

    def sort(self, key, reverse=False):
        students = []
        temp = self.head

        while temp:
            students.append((temp.roll, temp.name, temp.marks))
            temp = temp.next

        if key == "marks":
            students.sort(key=lambda x: x[2], reverse=reverse)
        else:
            students.sort(key=lambda x: x[0], reverse=reverse)

        self.head = None
        for roll, name, marks in students:
            self.add(roll, name, marks)


s = StudentList()

while True:
    print("\n1. Add")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Display")
    print("6. Sort")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = int(input("Roll No: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        s.add(roll, name, marks)
    elif ch == 2:
        roll = int(input("Enter Roll No: "))
        s.delete(roll)
    elif ch == 3:
        roll = int(input("Enter Roll No: "))
        name = input("Enter New Name: ")
        marks = float(input("Enter New Marks: "))
        s.update(roll, name, marks)
    elif ch == 4:
        roll = int(input("Enter Roll No: "))
        s.search(roll)
    elif ch == 5:
        s.display()
    elif ch == 6:
        key = input("Sort by roll or marks: ").lower()
        order = input("Ascending or descending: ").lower()
        s.sort(key, order == "descending")
        print("Records Sorted")
    elif ch == 7:
        break
    else:
        print("Invalid choice")
