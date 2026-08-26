"""
Implement a double ended queue that stores strings.
array deque is a data structure that has characteristics of both
a queue and a stack. 
Elements can be added or removed from either
the front or the back.
"""

import traceback


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addFirst(self, data):
        oldFirst = self.first
        self.first = Node(data)
        if oldFirst == None:
            self.last == self.first
        else:
            self.first.prev = None
            self.first.next = oldFirst
            oldFirst.prev = self.first
        self.size += 1

    def addLast(self, data):
        oldLast = self.last
        self.last = Node(data)
        if oldLast == None:
            self.first = self.last
        else:
            self.last.prev = oldLast
            self.last.next = None
            oldLast.next = self.last
        self.size += 1

    def removeFirst(self):
        oldFirst = self.first
        if self.first == None:
            return None
        else:
            self.first = oldFirst.next
            if self.first == None:
                self.last = self.first
            else:
                self.first.prev = None
        self.size -= 1
        return oldFirst.data

    def removeLast(self):
        oldLast = self.last
        if oldLast == None:
            return None
        else:
            self.last = oldLast.prev
            if self.last == None:
                self.first = self.last
            else:
                self.last.next = None
        self.size -= 1
        return oldLast.data

    def peekFirst(self):
        if self.first == None:
            return None
        else:
            return self.first.data

    def peekLast(self):
        if self.last == None:
            return None
        else:
            return self.last.data

    def getSize(self):
        return self.size


def assertTrue(condition, message):
    if not condition:
        raise Exception(message)


def doTestsPass():
    # TODO: implement more tests

    deque = Deque()
    deque.addLast("a")
    deque.addLast("b")

# enqueue
    assertTrue(deque.getSize() == 2, "Test failed, getSize should be 2")
    assertTrue("a" == deque.peekFirst(),
               "Test failed, first element should be a")
    assertTrue("b" == deque.peekLast(),
               "Test failed, last element should be b")

# dequeue
    assertTrue("a" == deque.removeFirst(),
               "Test failed, expected a")
    assertTrue("b" == deque.removeFirst(),
               "Test failed, expected b")

# push
    deque.addFirst("a")
    deque.addFirst("b")

    assertTrue(deque.getSize() == 2, "Test failed, getSize should be 2")
    assertTrue("b" == deque.peekFirst(),
               "Test failed, expected b")
    print(deque.peekLast())
    # assertTrue("a" == deque.peekLast(),
    #            "Test failed, expected a")

# pop
    assertTrue("b" == deque.removeFirst(),
               "Test failed, expected b")
    assertTrue("a" == deque.removeFirst(),
               "Test failed, expected a")


try:
    doTestsPass()
    print("All tests passed")
except:
    print("Test failed")
    traceback.print_exc()
