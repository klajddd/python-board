# OPTIMAL SOLUTION:

# time O(n) at worst, O(log n) at average
# space O(1)


class Solution:
    def inoderSuccessor(self, root, p):
        result = None
        current = root

        while current:
            if current.value > p.value:
                result = current
                current = current.left
            else:
                current = current.right

        return result

# BRUTE FORCE
# Time O(n)
# Space O(n)
# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         if root is None:
#             return None
#         nodes = []
#         nodes = self.inorderTraversal(root, nodes)
#         for i, n in enumerate(nodes):
#             if n is p:
#                 if len(nodes)-1 <= i:
#                     return None
#                 else:
#                     return nodes[i+1]
#         return None

#     def inorderTraversal(self, root, nodes):
#         if root.left:
#             self.inorderTraversal(root.left, nodes)

#         nodes.append(root)

#         if root.right:
#             self.inorderTraversal(root.right, nodes)
#         return nodes


class TreeNode:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(11)

    d = TreeNode(4)
    e = TreeNode(6)

    f = TreeNode(8)
    g = TreeNode(13)

    h = TreeNode(12)
    i = TreeNode(14)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f
    c.right = g

    g.left = h
    g.right = i

    sol = Solution()
    print(sol.inoderSuccessor(a, c).val)
