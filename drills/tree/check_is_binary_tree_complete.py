# Checking if a binary tree is a complete binary tree in C
class Node:

    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None


# Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


# Check if the tree is complete binary tree
def is_complete(root, index, node_count):

    # Check if the (sub)tree is empty
    if root is None:
        return True

    if index >= node_count:
        return False

    return is_complete(root.left, 2 * index + 1, node_count) and is_complete(root.right, 2 * index + 2, node_count)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("Complete binary tree")
else:
    print("NOT a complete binary tree")