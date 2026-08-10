class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # time O(n) as we need to traverse all nodes
    # space O(d) where d is depth
    # ==================================================================================================================
def validateBst(tree):
    # Write your code here.
    return helper_validateBst(tree, float('-inf'), float('inf'))


def helper_validateBst(tree, lowLimit, highLimit):
    if tree is None:
        return True

    if tree.value < lowLimit or tree.value > highLimit:
        return False

    return helper_validateBst(tree.left, lowLimit, tree.value - 1) \
           and helper_validateBst(tree.right, tree.value, highLimit)






# time O(n) as we need to traverse all nodes
# space O(n)
# ==================================================================================================================

def isValidBST_sort_list(root) -> bool:
    nodeList = []
    nodeList = helper_isValidBST_sort_list(nodeList, root)

    for i in range(1, len(nodeList)):
        if nodeList[i - 1] >= nodeList[i]:
            return False
    return True


def helper_isValidBST_sort_list(nodeList, node):

    if node.left:
        helper_isValidBST_sort_list(nodeList, node.left)

    nodeList.append(node.val)

    if node.right:
        helper_isValidBST_sort_list(nodeList, node.right)

    return nodeList














'''
{
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": null, "value": 22},
      {"id": "13", "left": null, "right": "14", "value": 13},
      {"id": "14", "left": null, "right": null, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": null, "value": 2},
      {"id": "1", "left": null, "right": null, "value": 1}
    ],
    "root": "10"
  }
}
'''