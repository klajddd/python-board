# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # time O(n)
    # space O(1)

    # [1, 2] <--- this would throw an error 'NoneType object has not attribute 'next'' if this while loop is used: 
    # while fast.next:

    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next: # fast could be null, that is why we check it is not null
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False


