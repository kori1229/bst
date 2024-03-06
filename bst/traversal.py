def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)
         
        # Visit node
        print(root.value,end=" ")
         
        # Traverse right subtree
        printInorder(root.right)
 
def printPreOrder(node):
    if node is None:
        return
    # Visit Node
    print(node.value, end = " ")
 
    # Traverse left subtree
    printPreOrder(node.left)
 
    # Traverse right subtree
    printPreOrder(node.right)

def printPostOrder(node):
    if node is None:
        return
 
    # Traverse left subtree
    printPostOrder(node.left)
 
    # Traverse right subtree
    printPostOrder(node.right)
     
    # Visit Node
    print(node.value, end = " ")
 