class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# In-order (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Pre-order (Root → Left → Right)
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# Post-order (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Level-order (BFS)
from collections import deque
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def delete_node(root, key):
    if not root:
        return None
    
    # Go left or right
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Found the node to delete
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Node with two children
        # Get inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # Replace root's value with successor's value
        root.value = successor.value
        # Delete successor
        root.right = delete_node(root.right, successor.value)
    
    return root


# Create BST
values = [20, 10, 30, 5, 15, 25, 35]
root = None
for val in values:
    root = insert(root, val)

# Traversals
print("In-order: ", end="")
inorder(root)
print("\nPre-order: ", end="")
preorder(root)
print("\nPost-order: ", end="")
postorder(root)
print("\nLevel-order: ", end="")
level_order(root)

print("\nBefore deletion (in-order): ", end="")
inorder(root)  # print current BST

root = delete_node(root, 8)

print("\nAfter deleting 8 (in-order): ", end="")
inorder(root)  # should show tree without 8

