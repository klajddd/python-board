'''
shift linked list by k nodes
1 2 3 4 5

if k = 2: then we get: 4 5 1 2 3
if k =-1: then we get: 2 3 4 5 1

'''


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None



# time O(k*n)
# space O(1)
def shiftLinkedList(head, k):
    # Write your code here.
    length = 1
    start = head
    theTail = None
    while start.next:
        start = start.next
        length += 1
    theTail = start
    k = k % length

    if k > 0:
        while k > 0:
            tail = head
            beforeTail = None
            while tail.next:
                beforeTail = tail
                tail = tail.next
            beforeTail.next = None
            tail.next = head
            head = tail
            k -= 1
        return head


    else:
        while k < 0:
            oldHead = head
            head = head.next
            theTail.next = oldHead
            theTail = theTail.next
            theTail.next = None
            k += 1
        return head

# COMPACT
# ======================================================================================================================
# O(n) time
# O(1) space
def shiftLinkedList_compact(head, k):
    # Write your code here.
    length = 1
    listTail = head

    while listTail.next:
        listTail = listTail.next
        length += 1

    offset = abs(k) % length

    if offset == 0:
        return head

    newTailPosition = length - offset if k >0 else offset
    newTail = head

    for i in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead