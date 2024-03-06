# Define a class called Node to represent a node in a binary search tree (BST)
class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)
