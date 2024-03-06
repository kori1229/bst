from node import Node

class Update:
    def __init__(self, bst):
        self.bst = bst

    # Method to update a value in the BST
    def update_value(self, old_value, new_value):
        self.bst.root = self._update_recursive(self.bst.root, old_value, new_value)

    # Helper method to recursively update a value in the BST
    def _update_recursive(self, node, old_value, new_value):
        if node is None:
            return node

        if old_value < node.value:
            node.left = self._update_recursive(node.left, old_value, new_value)
        elif old_value > node.value:
            node.right = self._update_recursive(node.right, old_value, new_value)
        else:
            # Node with the old value found, update it with the new value
            node.value = new_value

        return node