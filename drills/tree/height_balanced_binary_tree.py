# a binary tree is height balanced if for each node, the diff between the height
# of its left and right subtrees is at most 1

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

# time O(n) - n number of nodes in binary tree
# space O(h)
def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (
        leftSubTreeInfo.isBalanced
        and rightSubTreeInfo.isBalanced
        and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    )
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(isBalanced, height)





