# Definition for singly-linked list.
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# COMPLEXITY
# time: O(max(m, n)
# space: O(max(m, n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = None
        current = None
        carry_over = 0

        while l1 or l2 or carry_over:

            if l1:
                carry_over += l1.val
                l1 = l1.next
            if l2:
                carry_over += l2.val
                l2 = l2.next

            node = ListNode(carry_over % 10)
            carry_over = carry_over // 10

            if head is None:
                head = node
                current = head
            else:
                current.next = node
                current = node

        return head


    def addTwoNumbers_concise(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)

            current = current.next

            carry = carry // 10

        return dummy.next
