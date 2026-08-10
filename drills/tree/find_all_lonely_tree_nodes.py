# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getLonelyNodes(self, root: TreeNode):

        def populate_lonely(root):
            nonlocal lonely_list
            if root:
                if root.left and not root.right:
                    lonely_list.append(root.left.val)
                if root.right and not root.left:
                    lonely_list.append(root.right.val)
                populate_lonely(root.left)
                populate_lonely(root.right)

        lonely_list = []

        populate_lonely(root)

        return lonely_list

    # def getLonelyNodes(self, root: TreeNode):
    #
    #     def populate_lonely(root):
    #         nonlocal lonely_list
    #         if root:
    #             if root.left and not root.right:
    #                 lonely_list.append(root.left.val)
    #             if root.right and not root.left:
    #                 lonely_list.append(root.right.val)
    #             populate_lonely(root.left)
    #             populate_lonely(root.right)
    #
    #     lonely_list = []
    #
    #     if root:
    #         if root.right and not root.left:
    #             lonely_list.append(root.right.val)
    #         if root.left and not root.right:
    #             lonely_list.append(root.left.val)
    #         populate_lonely(root.left)
    #         populate_lonely(root.right)
    #
    #     return lonely_list



import unittest

class TestTree(unittest.TestCase):

    def testTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.left.left.left = TreeNode(7)

        s = Solution()
        self.assertEqual(s.getLonelyNodes(root), [7, 6], 'Test tree failed')

if __name__ == "__main__":
    unittest.main()