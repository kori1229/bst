from binary_search_tree import BinarySearchTree
from node import Node

# Insert a value into the BST
def insert(bst, value):
    # If the root is None, create a new node with the given value as the root
    if bst.root is None:
        bst.root = Node(value)
    else:
        _insert_recursive(bst.root, value)

# Helper method to recursively insert a value into the BST
def _insert_recursive(node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            _insert_recursive(node.left, value)
    elif value > node.value:
        if node.right is None:
            node.right = Node(value)
        else:
            _insert_recursive(node.right, value)
