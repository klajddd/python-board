# read again to understand it

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# ======================================================================================================================


# O(h) time ---> h = height of the tree
# O(1) space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)

def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent

# ======================================================================================================================

# time O(n)
# space O(n)
def findSuccessor(self, tree, node):
    # Write your code here.
    nodes = []
    nodes = self.getNodes(tree, nodes)

    for i in range(len(nodes)):
        if nodes[i] == node and i <= len(nodes) - 2:
            return nodes[i + 1]

    return None

def getNodes(self, tree, nodes):
    if tree is None:
        return nodes

    self.getNodes(tree.left, nodes)
    nodes.append(tree)
    self.getNodes(tree.right, nodes)

    return nodes


# six = BinaryTree(6, None, None, four)
# five = BinaryTree(5, None, None, two)
# four = BinaryTree(4, six, None, two)
# three = BinaryTree(3, None, None, one)
# two = BinaryTree(2, four, five, one)
# one = BinaryTree(1, two, three)
# node = 5
# result = 1
