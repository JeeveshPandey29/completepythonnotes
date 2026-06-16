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


class BSTNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, v):
        if not root:
            return BSTNode(v)
        if v < root.val:
            root.left = self.insert(root.left, v)
        elif v > root.val:
            root.right = self.insert(root.right, v)
        return root

    # Search
    def search(self, root, key):
        if not root:
            return False
        if root.val == key:
            return True
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Delete
    def delete(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: No child
            if not root.left and not root.right:
                return None
            # Case 2: One child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Two children → replace with inorder successor
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# AVL TREES

class AVLNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def avl_insert(node, key):
    if not node:
        return AVLNode(key)

    if key < node.val:
        node.left = avl_insert(node.left, key)
    elif key > node.val:
        node.right = avl_insert(node.right, key)
    else:
        return node

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and key < node.left.val:
        return right_rotate(node)
    if balance < -1 and key > node.right.val:
        return left_rotate(node)
    if balance > 1 and key > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def avl_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def avl_delete(node, key):
    if not node:
        return node

    if key < node.val:
        node.left = avl_delete(node.left, key)
    elif key > node.val:
        node.right = avl_delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp = avl_min_value_node(node.right)
        node.val = temp.val
        node.right = avl_delete(node.right, temp.val)

    if not node:
        return node

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


# Example usage of AVL tree
avl_root = None
for value in [10, 20, 30, 40, 50, 25]:
    avl_root = avl_insert(avl_root, value)

print("\nAVL Tree Inorder:")
inorder(avl_root)
print("\nAVL Tree Preorder:")
preorder(avl_root)

avl_root = avl_delete(avl_root, 40)
print("\nAVL Tree Inorder after deleting 40:")
inorder(avl_root)
print()

