# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k: int):

        if head is None:
            return None

        if head and not head.next:
            return head

        current = head

        nodes = 1

        while current.next:
            current = current.next
            nodes += 1

        tail = current
        k = k % nodes

        repeat_rotation = nodes - k

        while repeat_rotation > 0:
            new_head = head.next
            head.next = None
            tail.next = head
            tail = head
            head = new_head
            repeat_rotation -= 1

        return head








