# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def addNodes(node):
            if node:
                if node.val >= low and node.val <= high:
                    nonlocal theSum
                    theSum += node.val

                if node.val > low:
                    addNodes(node.left)
                if node.val < high:
                    addNodes(node.right)

        theSum = 0
        addNodes(root)
        return theSum

one = TreeNode(10)
two = TreeNode(5)
three = TreeNode(15)
one.left = two
one.right = three
four = TreeNode(3)
five = TreeNode(7)
two.left = four
two.right = five

s = Solution()

print(s.rangeSumBST(one, 5, 14))

assert s.rangeSumBST(one, 5, 14) == 22