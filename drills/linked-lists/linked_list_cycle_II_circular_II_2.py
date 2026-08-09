# time O(n)
# space O(1)


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        intersectionNode = self.detectIntersection(head)
        current = head

        if intersectionNode is None:
            return None

        while current is not intersectionNode:
            current = current.next
            intersectionNode = intersectionNode.next
        return intersectionNode

    def detectIntersection(self, head: ListNode) -> ListNode:
        # Floyd's algorithm
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return slow
        return None
