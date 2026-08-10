class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
time: O(n)
space: O(n) for the stack, in UNBALANCED TREEs, worst case scenario, space is the height of the tree = O(n)
space: O(log(n)) best/average when the tree is balanced, stack space is the height of the tree = O(log(n)) 
'''
class Solution:
    def binaryTreePaths(self, root):

        paths = []
        self.construct_paths(root, '', paths)
        return paths

    def construct_paths(self, root, path, paths):
        if root:
            path += str(root.val)

            if root.left or root.right:
                path += '->'  # extend the current path
                self.construct_paths(root.left, path, paths)
                self.construct_paths(root.right, path, paths)
            else:
                paths.append(path)

one = TreeNode(10)
two = TreeNode(5)
three = TreeNode(15)
one.left = two
one.right = three
four = TreeNode(3)
five = TreeNode(7)
two.left = four
two.right = five

s = Solution()

print(s.binaryTreePaths(one))