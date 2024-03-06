from node import Node

# delete a node with a specific value from the BST
def delNode(bst, value):
    bst.root = _delNode(bst.root, value)

# recursively delete a node with a specific value from the BST
def _delNode(node, value):
    if node is None:
        return node

    # Traversinh to the node to be deleted
    if value < node.value:
        node.left = _delNode(node.left, value)
    elif value > node.value:
        node.right = _delNode(node.right, value)
    else:
        # Node found, deleting
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # Node has two children, find the inorder successor (smallest in the right subtree)
        temp = minValueNode(node.right)

        # Copy the inorder successor's content to this node
        node.value = temp.value

        # Delete the inorder successor
        node.right = _delNode(node.right, temp.value)

    return node

# Helper method to find the minimum value node in a subtree (used for finding inorder successor)
def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current