# Definition for singly-linked list.

'''
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the probabilities of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode()
        dummy.next = head

        pre_left = dummy
        pre_right = dummy
        left = head
        right = head

        for i in range(1, k):
            pre_left = pre_left.next
            left = left.next

        null_check = left

        while null_check.next:
            pre_right = pre_right.next
            right = right.next
            null_check = null_check.next

        # check for node being in the middle
        if left == right:
            return head

        pre_left.next = right
        pre_right.next = left

        self.swap(left, right)

        return dummy.next

    def swap(self, left, right):
        temp = left.next
        left.next = right.next
        right.next = temp




    def swapNodes_VALUES(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode()
        dummy.next = head
        slow_dummy = ListNode()
        slow_dummy.next = head

        for i in range(k):
            dummy = dummy.next

        first_node = dummy

        while dummy:
            dummy = dummy.next
            slow_dummy = slow_dummy.next

        temp = first_node.val
        first_node.val = slow_dummy.val
        slow_dummy.val = temp

        return head