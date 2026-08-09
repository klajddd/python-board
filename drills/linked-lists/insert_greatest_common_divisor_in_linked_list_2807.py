from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - check if current node is None and if there is a next node
        - value of current
        - value of next
        - find the GCD -> create a method that finds the GCD
        - create a node with GCD value and put it in the LL
        - the go next, next
        '''
        def findGcdValue(val1, val2):
            if val2 == 0:
                return val1
            else:
                return findGcdValue(val2, val1 % val2)

        start = head
        run = True
        while run:
            if head is not None and head.next is not None:
                gcdValue = findGcdValue(head.val, head.next.val)
                newNode = ListNode(gcdValue, head.next)
                head.next = newNode
                head = head.next.next
            else:
                run = False

        return start

        