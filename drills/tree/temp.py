# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# time O(n)
# space worst case: O(n) 1 long branch,,, don't get confused with usual time complx log(n) if a good complete-ish tree
# ----------------------------------------------------------------------------------------------------------------------
def branchSums(root):
    # Write your code here.
    if root is None:
        return []
    result = []
    result = helper(root, result, 0)
    return result


def helper(root, result, total):
    total += root.value

    if root.left is None and root.right is None:
        result.append(total)
        total -= root.value
    if root.left:
        helper(root.left, result, total)
    if root.right:
        helper(root.right, result, total)
    return result

import unittest

class TestSums(unittest.TestCase):
    def testSums(self):
        res = branchSums(one)
        print(res)
        self.assertEqual(1, 1)

one = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
eight = BinaryTree(8)
nine = BinaryTree(9)
ten = BinaryTree(10)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
four.left = eight
four.right = nine
five.left = ten