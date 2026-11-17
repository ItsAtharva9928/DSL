class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def minValueNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


tree = BST()
root = None

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter value: "))
        root = tree.insert(root, key)
    elif ch == 2:
        key = int(input("Enter value: "))
        root = tree.delete(root, key)
        print("Node Deleted")
    elif ch == 3:
        key = int(input("Enter value: "))
        if tree.search(root, key):
            print("Node Found")
        else:
            print("Node Not Found")
    elif ch == 4:
        print("Inorder Traversal:")
        tree.inorder(root)
        print()
    elif ch == 5:
        print("Preorder Traversal:")
        tree.preorder(root)
        print()
    elif ch == 6:
        print("Postorder Traversal:")
        tree.postorder(root)
        print()
    elif ch == 7:
        break
    else:
        print("Invalid choice")
