# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # time O(n) for worst case UNBALANCED TREE, BST where parents have 1 child node
    # time O(h) = O(log(n))
    # O(h) is similar to saying O(log n), since a balanced tree of height h will have (roughly) 2^h nodes
    # space O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return

        if p and not q:
            return p

        if q and not p:
            return q

        if not p and not q:
            return None

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


