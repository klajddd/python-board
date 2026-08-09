# Definition for singly - linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# time: O(n) where n is total nodes in linked list
# space: O(1)

class Solution:

    def removeNthFromEnd_one_traversal(self, head: ListNode, n: int) -> ListNode:
        # dummy created for case where input has a single node
        dummy = ListNode()

        dummy.next = head

        fast = dummy
        slow = dummy

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd_concise(self, head: ListNode, n: int) -> ListNode:

        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head

        count = 0

        node = head

        while node:
            count += 1
            node = node.next

        count = count - n
        node = dummy

        while count > 0:
            node = node.next
            count -= 1

        node.next = node.next.next
        return dummy.next


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if head is None:
            return None

        count = 0
        node = head

        while node:
            count += 1
            node = node.next

        if count == 1:
            return None

        if count == n:
            return head.next

        remove_next = count - n

        node = head

        while remove_next > 1:
            node = node.next
            remove_next -= 1

        node.next = node.next.next

        return head

if __name__ == '__main__':
    s = Solution()
    print(s.removeNthFromEnd_concise(None, 0))





