def reverse_linked_list(head):

    # time O(n)
    # space O(1)

    # Reverse the linked list in place
    # [5] - [4] - [3] - [2] - [1]
    prev = None
    current = head # old head

    while current is not None:

        next = current.next
        current.next = prev
        prev = current
        current = next

    # return head of list
    return prev


class Solution:
    def reverseList(self, head):

        if head is None:
            return

        previous = None
        current = head
        next = current.next

        while current is not None:
            current.next = previous
            previous = current
            current = next
            if next is None:
                break
            else:
                next = next.next

        return previous


# =============================== TESTING =========================



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import unittest

class TestSum(unittest.TestCase):

    e = Node(5)
    d = Node(4, e)
    c = Node(3, d)
    b = Node(2, c)
    a = Node(1, b)
    s = Solution()


    def test_reverse_linked_list(self):
        self.assertEqual(self.s.reverseList(self.a), self.e, 'should be e=5')

if __name__=='__main__':
    unittest.main()

'''
    def reverse_linked_list(self):
        
        node1 = None
        node2 = self.head
        
        while node2 is not None:
        
            node3 = node2.next
        
            node2.next = node1
        
            node1 = node2
        
            node2 = node3
       
        return node1

        '''
