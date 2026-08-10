# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if not root1 and not root2:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        result_root = TreeNode(root1.val if root1 else 0 + root2.val if root2 else 0)

        result_root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        result_root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return result_root


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if root1 and root2:

            result_root = TreeNode(root1.val + root2.val)
            result_root.left = self.mergeTrees(root1.left, root2.left)
            result_root.right = self.mergeTrees(root1.right, root2.right)

            return result_root

        else:
            return root1 or root2