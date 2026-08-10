# Definition for a binary tree node.
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, targetSum):
        paths = []
        self.pathToTargetSum(root, targetSum, [], paths)
        return paths



five = TreeNode(5)
four = TreeNode(4)
eight = TreeNode(8)
five.left = four
five.right = eight

eleven = TreeNode(11)
four.left = eleven

thirteen = TreeNode(13)
four_2 = TreeNode(4)
eight.left = thirteen
eight.right = four_2


seven = TreeNode(7)
two = TreeNode(2)
eleven.left = seven
eleven.right = two

five_2 = TreeNode(5)
one = TreeNode(1)
four_2.left = five_2
four_2.right = one

s = Solution()
print(s.pathSum(five, 22))

