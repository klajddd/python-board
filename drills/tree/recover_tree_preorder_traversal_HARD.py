# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        Input: traversal =

        "1-401--349---90--88
         ^                                       '''
    def recoverFromPreorder(self, traversal: str) -> TreeNode:

        '''
            Input: traversal =

            "1-401--349---90--88
             ^                                       '''
        stack = []
        i = 0

        while i < len(traversal):

            level = 0
            val = ""

            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1

            while i < len(traversal) and traversal[i] != '-':
                val += traversal[i]
                i += 1

            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)

            if not stack:
                stack.append(node)
                continue

            if stack[-1].left is None:
                stack[-1].left = node

            else:
                stack[-1].right = node
            stack.append(node)

        return stack[0]


input = "1-401--349---90--88"

s = Solution()

a = s.recoverFromPreorder(input)

print(a)




















