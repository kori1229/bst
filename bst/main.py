    # Now you can perform other operations on the binary search tree, such as searching, deleting, etc.
from binary_search_tree import BinarySearchTree
from node import Node
from insert import insert
from search import search
from build_tree import build_tree_from_input
from traversal import printInorder, printPreOrder, printPostOrder
from delete import delNode
from update import Update

if __name__ == "__main__":
    bst = BinarySearchTree()
    update = Update(bst)

    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert a value")
        print("2. Search for a value")
        print("3. Print the tree in different orders")
        print("4. Delete a value")
        print("5. Update a value")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter a value to insert: "))
            insert(bst, value)
        elif choice == '2':
            value = int(input("Enter a value to search: "))
            result = search(bst, value)
            if result:
                print(f"Value {value} found in the tree.")
            else:
                print(f"Value {value} not found in the tree.")
        elif choice == '3':
            print("\nInorder Traversal:")
            printInorder(bst.root)
            
            print("\nPreorder Traversal:")
            printPreOrder(bst.root)
            
            print("\nPostorder Traversal:")
            printPostOrder(bst.root)
        elif choice == '4':
            value = int(input("Enter a value to delete: "))
            delNode(bst, value)
        elif choice == '5':
            old_value = int(input("Enter the value you want to update: "))
            new_value = int(input("Enter the new value you want to update to: "))
            update.update_value(old_value, new_value)
            print("Value updated successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")