# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # space: worst case O(n)
    # time: O(n)
    def isUnivalTree(self, root: TreeNode) -> bool:
        vals = set()

        def dfs(root):
            if root:
                vals.add(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        return len(vals) == 1

    # space: worst case O(n)
    # time: O(h)
    def dfs_isUnivalTree_o_h_space(self, root: TreeNode):

        if not root:
            return True

        if root.right:
            if root.val != root.right.val:
                return False

        if root.left:
            if root.val != root.left.val:
                return False

        self.dfs_isUnivalTree_o_h_space(root.left) and self.dfs_isUnivalTree_o_h_space(root.right)

    # space: worst case O(n)
    # time: O(n)
    def bfs_isUnivalTree_o_n_space(self, root):
        import collections
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if node.val != root.val:
                return False
            # if node.left:
            #     dq.append(node.left)
            # if node.right:
            #     dq.append(node.right)
            dq.extend([n for n in (node.left, node.right) if n])
        return True


# TESTING ==============================================================================================================

import unittest

class TestSolution(unittest.TestCase):

    def testTreeFalseCase(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root.right.left = TreeNode(6)

        root.left.left.left = TreeNode(7)

        s = Solution()

        self.assertEqual(s.isUnivalTree(root), False, "False case failed")

    def testTreeTrueCase(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)

        root.right.left = TreeNode(1)

        root.left.left.left = TreeNode(1)

        s = Solution()
        self.assertEqual(s.isUnivalTree(root), True, "True case failed")

    def test_bfs(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)

        root.right.left = TreeNode(1)

        root.left.left.left = TreeNode(1)
        s = Solution()
        self.assertEqual(s.bfs_isUnivalTree_o_n_space(root), True, "BFS true case failed")

if __name__ == "__main__":
    unittest.main()



