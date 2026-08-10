class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #     time: O(h) where h is the height of the tree (best case this is O(log n))
    #     space O(1)
    def inorderSuccessor_time_oh_space_1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        result = None

        while root:

            if root.val > p.val:
                result = root
                root = root.left
            else:
                root = root.right

        return result


    # time: O(n)
    # space: O(n)
    def inorderSuccessor_time_on_space_on(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # Definition for a binary tree node.
        inOrder = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            inOrder.append(root)
            dfs(root.right)

        dfs(root)
        result = TreeNode(float('inf'))

        for node in inOrder:
            if node.val > p.val and node.val < result.val:
                result = node

        if result.val <= p.val or result.val == float('inf'):
            return None
        return result

    # time O(n)
    # space O(n) for second case and therefore overall
    # space O(1) only for first case
    previous = None
    inorder_successor = None
    def inorderSuccessor_without_bst_properties(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        self.previous = None
        self.inorder_successor = None

        if p.right:
            self.inorder_successor = p.right
            while self.inorder_successor.left:
                self.inorder_successor = self.inorder_successor.left

        else:
            self.inorderCase2(root, p)

        return self.inorder_successor

    def inorderCase2(self, node: 'TreeNode', p: 'TreeNode'):

        if not node:
            return

        self.inorderCase2(node.left, p)

        # Check if previous is the inorder predecessor of node
        if self.previous == p and self.inorder_successor is None:
            self.inorder_successor = node
            return

        # Keeping previous up-to-date for further recursions
        self.previous = node

        # Recurse on the right side
        self.inorderCase2(node.right, p)

if __name__=='__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    s = Solution()

    print(s.inorderSuccessor(root, root.left).val)

