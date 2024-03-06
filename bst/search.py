# Search for a value in the BST
def search(bst, value):
    return _search_recursive(bst.root, value)

# Helper method to recursively search for a value in the BST and return the node if found
def _search_recursive(node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return _search_recursive(node.left, value)
    else:
        return _search_recursive(node.right, value)
