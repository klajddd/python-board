class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# time O(n)
# space O(n)
def removeDuplicatesFromLinkedList(node):
    if node is None:
        return None

    set_values = set()
    set_values.add(node.value)

    head = node

    while node and node.next:
        if node.next.value in set_values:
            node.next = node.next.next
        else:
            set_values.add(node.next.value)
            node = node.next
    return head