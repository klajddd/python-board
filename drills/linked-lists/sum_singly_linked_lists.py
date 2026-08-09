# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# time O max(n, m)
# space O max(n, m)
# more concise, same space-time
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    headPointer = LinkedList(0)
    currentNode = headPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne or nodeTwo or carry != 0:
        valueOne = nodeOne.value if nodeOne else 0
        valueTwo = nodeTwo.value if nodeTwo else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None

    return headPointer.next



# less concise, same space-time
# ----------------------------------------------------------------------------------------------------------------------

# time O max(n, m)
# space O max(n, m)
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    if not linkedListOne and not linkedListTwo:
        return None
    if not linkedListOne:
        return linkedListTwo
    if not linkedListTwo:
        return linkedListOne

    carry = 0
    currentNodeListOne = linkedListOne
    currentNodeListTwo = linkedListTwo
    sumDigits = []
    while currentNodeListOne or currentNodeListTwo:
        total = carry
        if currentNodeListOne and currentNodeListTwo:
            total += currentNodeListOne.value + currentNodeListTwo.value
            currentNodeListOne = currentNodeListOne.next
            currentNodeListTwo = currentNodeListTwo.next
        elif currentNodeListOne:
            total += currentNodeListOne.value
            currentNodeListOne = currentNodeListOne.next
        else:
            total += currentNodeListTwo.value
            currentNodeListTwo = currentNodeListTwo.next

        if total > 9:
            sumDigits.append(total - 10)
            carry = 1
        else:
            sumDigits.append(total)
            carry = 0
    tailNode = None
    if carry > 0:
        tailNode = LinkedList(1)

    currentNode = LinkedList(sumDigits[-1])
    currentNode.next = tailNode

    for i in range(len(sumDigits) - 2, -1, -1):
        newNode = LinkedList(sumDigits[i])
        newNode.next = currentNode
        currentNode = newNode

    return currentNode

'''
OUTPUT
{
  "head": "1",
  "nodes": [
    {"id": "1", "next": "9", "value": 1},
    {"id": "9", "next": "2", "value": 9},
    {"id": "2", "next": "2-2", "value": 2},
    {"id": "2-2", "next": null, "value": 2}
  ]
}
RESULT 1742 + 549 = 2291

INPUT
{
  "linkedListOne": {
    "head": "2",
    "nodes": [
      {"id": "2", "next": "4", "value": 2},
      {"id": "4", "next": "7", "value": 4},
      {"id": "7", "next": "1", "value": 7},
      {"id": "1", "next": null, "value": 1}
    ]
  },
  "linkedListTwo": {
    "head": "9",
    "nodes": [
      {"id": "9", "next": "4", "value": 9},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": null, "value": 5}
    ]
  }
}
'''










