# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time: O(n)
# space: O(h)
class Solution:
    def goodNodes_bfs_preorder(self, root: TreeNode) -> int:

        if root is None:
            return 0

        result = 0
        maximum = root.val

        def dfs(node, maximum):
            nonlocal result
            if node is None:
                return
            if node.val >= maximum:
                result += 1
                maximum = max(maximum, node.val)
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, maximum)

        return result

    def goodNodes_easier_to_read_less_efficient(self, root: TreeNode) -> int:

        if root is None:
            return 0

        result = 0

        def dfs(node, maximum):
            nonlocal result
            if node.val >= maximum:
                result += 1
            if node.left:
                dfs(node.left, max(maximum, node.left.val))
            if node.right:
                dfs(node.right, max(maximum, node.right.val))

        dfs(root, root.val)

        return result