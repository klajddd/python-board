# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The LCA is defined between two nodes p and q as the lowest node in T that has both p and q as 
descendants, where we allow a node to be a descendant of itself.
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None

        def findLCA(root, p, q):
            if root:
                temp = root.val
            if root is None:
                return False
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            current_node = False
            # boolean check root's val, if root itself is p/q
            if root == p or root == q:
                current_node = True

            # check if root is p/q and if any of the left/right contain p/q
            if ((left and right) or (left and current_node) or (right and current_node)):
                nonlocal result
                result = root
                return

            # if left and right side don't contain p/q, or left/right does not contain p/q and root itself is not p/q
            # return if only 1 side contains p/q or if current node is p/q
            return (left or right or current_node)

        findLCA(root, p, q)
        return result


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.left.left = None
root.left.left.right = None
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

s = Solution()
result = s.lowestCommonAncestor(root, root.left, root.right)
assert result.val == 3
print(result.val)