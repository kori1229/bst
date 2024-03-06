from insert import BinarySearchTree, insert

# Method to take user input and build a binary search tree
def build_tree_from_input():
    bst = BinarySearchTree()
    print("Enter values to insert into the binary search tree (type 'done' when finished):")
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            insert(bst, value)
        except ValueError:
            print("Invalid input! Please enter an integer value.")
    return bst
