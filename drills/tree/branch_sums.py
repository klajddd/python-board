# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    branchSumsHelper(root, 0, result)
    return result


def branchSumsHelper(node, runningSum, result):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if not node.left and not node.right:
        result.append(newRunningSum)
        return result

    if node.left:
        branchSumsHelper(node.left, newRunningSum, result)
    if node.right:
        branchSumsHelper(node.right, newRunningSum, result)


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
branchSums(one)

a = branchSums(one)
print(a)
