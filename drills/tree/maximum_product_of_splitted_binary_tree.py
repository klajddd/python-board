# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def best_maxProduct(self, root) -> int:
        vals = []

        def fn(node):
            """Return sum of sub-tree."""
            if not node: return 0
            ans = node.val + fn(node.left) + fn(node.right)
            vals.append(ans)
            return ans

        total = fn(root)
        return max((total - x) * x for x in vals) % 1_000_000_007


    def first_maxProduct(self, root):



# =============================================================================================
array = [1,2,3,4,5,6]

s = Solution()

print(s.maxProduct(array))