class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0

    def removeNode(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre

    def addNode(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def update(self, node):
        self.removeNode(node)
        self.addNode(node)

    def insert(self, node):
        self.addNode(node)
        self.count += 1
        return node

    def removeLast(self):
        last = self.tail.pre
        self.removeNode(last)
        self.count -= 1
        return last


class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.dic = {}
        self.cap = capacity

    # time O(1)
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.dll.update(node)
            return node.value
        else:
            return -1

    # time O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.dll.update(node)
        else:
            if self.dll.count == self.cap:
                last = self.dll.removeLast()
                del self.dic[last.key]
            node = Node(key, value)
            self.dic[key] = node
            self.dll.insert(node)