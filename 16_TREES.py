class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# Example Tree:
#           A
#         /   \
#        B     C
#       / \      \
#      D   E      F
#         / \
#        G   H

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.left.right.left = Node("G")
root.left.right.right = Node("H")
root.right.right = Node("F")

print("Preorder: ")
preorder(root)   # A B D E G H C F
print("\nInorder: ")
inorder(root)    # D B G E H A C F
print("\nPostorder: ")
postorder(root)  # D G H E B F C A

