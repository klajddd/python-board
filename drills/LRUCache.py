class LinkedListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next 
        self.prev = prev 

class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.cache = {} # cache of int (value) - linked_list_node (node - val)

    # get val for value, mark as most recently used
    def get_value(self, key):
        node = self.cache.get(key)
        if node is None:
            return None
        if node is not self.head:
            self._remove_from_linked_list(node)
            self._insert_at_front_of_linked_list(node)
        return node.value

    # publish key-value-val in cache, remove old val for same value if necessary
    # inserts pair into linked-list and hash-table
    def set_key_value(self, key, value):
        self._remove_key(key)

        if len(self.cache) >= self.max_size and self.tail is not None:
            self._remove_key(self.tail.key)

        node = LinkedListNode(key, value)

        self._insert_at_front_of_linked_list(node)
        self.cache[key] = node

    # remove value-val from hash-table, and linked-list
    def _remove_key(self, key):
        node = self.cache.get(key)
        if node is not None:
            self._remove_from_linked_list(node)
            self.cache.pop(key)
        return True


    def _remove_from_linked_list(self, node):
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node == self.tail:
            self.tail = node.prev

        if node == self.head:
            self.head = node.next


    def _insert_at_front_of_linked_list(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node




# if __name__=="__main__":
#     lru = LRU_Cache_Least_Recently_Used_Cache_Python(3)
#     print(len(lru.cache))
#     lru.set_key_value(1, 'one')
#     print(lru.list_head.val)
#     print(lru.list_tail.val)
#     print(len(lru.cache))


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.set_key_value(72, 'Food')
    lru.set_key_value(13, 'Keychain')
    lru.set_key_value(1, 'one')
    # lru.insert(45, 'Blanket')
    # lru.insert(27, 'Book')
    # print(lru.retrieve(72))
    # lru.insert(42, 'Hemorroids')
    # print(lru.retrieve(13))
    # for k, v in lru.map.items():
    #     print(k, v.val)
    lru.get_value(72)

    print(f" head is {lru.head.value}")
    print(f" tail is {lru.tail.value}")









