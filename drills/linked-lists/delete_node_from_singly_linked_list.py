import unittest


class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = NoneCharles Curley



a = LinkedListNode('array')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

# time O(1)
# space O(1)


def delete_node(node_to_delete):

        # Delete the input node from the linked list
    next_node = node_to_delete.next

    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next

    else:
        raise Exception("Can't delete the last node with this technique!")


delete_node(b)
