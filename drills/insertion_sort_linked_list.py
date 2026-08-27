

# time : O(n^2)
# space : O(1)

class Solution:
    def insertionSortList(self, head):

        dummy_head = ListNode(0)

        dummy_head.next = head

        node_to_insert = head

        while head and head.next:

            if head.val > head.next.value:

                # Locate node_to_insert.
                node_to_insert = head.next

                # Locate node_to_insert_pre.
                node_to_insert_pre = dummy_head

                while node_to_insert_pre.next.value < node_to_insert.value:

                    node_to_insert_pre = node_to_insert_pre.next

                head.next = node_to_insert.next # rewiring
                node_to_insert.next = node_to_insert_pre.next # Insert node_to_insert between node_to_insert_pre and node_to_insert_pre.next.
                node_to_insert_pre.next = node_to_insert

            else:
                head = head.next

        return dummy_head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
