class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, invert the tree, and return its root.
'''
            1                               1
          /   \                           /   \
         2     3          ----->         3     2
       /   \                           /   \
      4    None                     None    4

'''
class Solution:

    # time O(n) - number of nodes
    # space O(h) - height of the tree, or O(log n) because ---> O(d) = O(log n)
    # dfs, pre-order
    def invertBinaryTree(self, tree):
        if tree.right or tree.left:
            tree.right, tree.left = tree.left, tree.right
        if tree.left:
            self.invertBinaryTree(tree.left)
        if tree.right:
            self.invertBinaryTree(tree.right)



    # time: O(n)
    # space: O(n)
    def invertTree_iterative_bfs(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = [root]

        while queue:
            current = queue.pop(0)
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root


    # time: O(n)
    # space: O(n)
    # The solution is BOUND TO THE APPLICATION STACK, meaning it is not scalable
    # the problem size will overflow the stack and crash your application, therefore use BFS / level-order-traversal.

    def invertTree_recursive_dfs(self, root: TreeNode) -> TreeNode:

        if not root: return

        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree_recursive_dfs(root.left)
            self.invertTree_recursive_dfs(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree_recursive_dfs(root.right)

        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree_recursive_dfs(root.left)

        return root


    # time: O(n)
    # space: O(n)
    def invertTree_recursive_dfs_concise(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = root.right
        root.right = self.invertTree_recursive_dfs_concise(root.left)
        root.left = self.invertTree_recursive_dfs_concise(temp)
        return root



if __name__ == '__main__':
    s = Solution()
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    one.left = two
    one.right = three
    print(s.invertTree_recursive_dfs_concise(one).val)
