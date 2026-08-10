"""
Given a BST and a target val, find the NODE with the closest val to the TARGET.
BST node val:
greater than LEFT nodes
smaller/EQUAL TO RIGHT nodes

"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# time: average = O(log n) = O(h)
# time: worst = O(n)
# space: O(1)
# space: if implementing RECURSIVELY, the space will be the same as the time complexity

def findClosestValueInBst(tree, target):

    difference = float('inf')
    result = float('inf')

    while tree:

        if abs(tree.value - target) < difference:
            difference = abs(tree.value - target)
            result = tree.value

        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            break

    return result




import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)