# Definition for singly-linked list.

class LinkedList:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = None
        
# ----------------------------------------------------------------------------------------------------------------------


# time: O(M + N)
# space: O(1)
def mergeLinkedLists(headOne, headTwo):
    head = None
    if headOne.value < headTwo.value:
        head = headOne
        headOne = headOne.next
    else:
        head = headTwo
        headTwo = headTwo.next

    current = head

    while headOne and headTwo:
        if headOne.value < headTwo.value:
            current.next = headOne
            current = headOne
            headOne = headOne.next
        else:
            current.next = headTwo
            current = headTwo
            headTwo = headTwo.next

    if headOne:
        current.next = headOne
    if headTwo:
        current.next = headTwo

    return head

# ----------------------------------------------------------------------------------------------------------------------


    # creating a new result list
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None

        node = LinkedList()
        result = node 
        
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    node.val = list1.val
                    list1 = list1.next
                else:
                    node.val = list2.val
                    list2 = list2.next
            elif list1:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            if list1 or list2:
                node.next = LinkedList()
            node = node.next
        return result


# ----------------------------------------------------------------------------------------------------------------------

# time: O(M + N)
# space: O(1)
def mergeTwoLists_compact(self, headOne, headTwo) -> LinkedList:

    dummy = temp = LinkedList(0)  # 0 does not matter, it is just a dummy node

    while headOne and headTwo:

        if headOne.val < headTwo.val:
            temp.next = headOne
            headOne = headOne.next

        else:
            temp.next = headTwo
            headTwo = headTwo.next

        temp = temp.next

    if headOne is None:
        temp.next = headTwo
    else:
        temp.next = headOne


    return dummy.next


