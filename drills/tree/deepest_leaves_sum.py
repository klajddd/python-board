# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root) -> int:

        max_depth = 0

        q = []

        q.append((root, 0))

        output = 0

        while len(q) > 0:

            curr, curr_depth = q.pop(0)

            if curr_depth > max_depth:
                max_depth = curr_depth
                output = 0

            if curr_depth == max_depth:
                output += curr.val

            if curr.left: q.append((curr.left, curr_depth + 1))
            if curr.right: q.append((curr.right, curr_depth + 1))

        return output