import unittest


# O(n) time
# O(1) space
def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list
    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: ' + str(k))
        # get list's length
    list_length = 1
    current_node = head
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    if k > list_length:
        raise ValueError('k larger than linked list length: ' + str(k))

    how_far_is_target = list_length - k
    current_node = head

    for i in range(how_far_is_target):
        current_node = current_node.next

    return current_node

# O(n) time
# O(1) space
# KEEPING array STICK APPROACH
# BETTER FOR PROCESSORS THAT USE LEAST RECENTLY USED 'LRU' CACHES
# AS THE TIME IS MUCH SHORTER WHEN WE FIRST AND LAST ACCESS THE SAME NODES


def kth_to_last_node_stick(k, head):

    # Return the kth to last node in the linked list
    if k < 1:
        raise ValueError(
            'Impossible to find less than first to last node: ' + str(k))

    left_node = head
    right_node = head

    for _ in range(k-1):
        if not right_node.next:
            raise ValueError(
                'k is larger than the length of the linked list: ' + str(k))

        right_node = right_node.next

    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

    return left_node


# time O(n)
# space O(n)
# O(n) SPACE APPROACH
def kth_to_last_node_O_n_space(k, head):

    # Return the kth to last node in the linked list

    lis = []
    current = head

    while current:
        lis.append(current)
        current = current.next
    return lis[len(lis) - k]


# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)
