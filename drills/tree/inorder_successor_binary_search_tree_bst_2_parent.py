
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



class Solution:
    # time O(h) where h is the depth of the BST
    #           time O(logN) in the best case
    #           time (N) in the worst case
    # space O(1)
    def inorderSuccessor(self, node: 'Node') -> 'Node':

        if node is None:
            returnp

        if node.right:
            node = node.right
            while node.left:
                node = node.left

            return node

        else:
            parent = node.parent
            while parent:
                if parent.val > node.val:
                    return parent
                parent = parent.parent


    # time O(h) where h is the depth of the BST
    #           time O(logN) in the best case
    #           time (N) in the worst case
    # space O(1)
    def inorderSuccessor_slightly_different(self, node: 'Node') -> 'Node':
        # the next_val is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # the next_val is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent





