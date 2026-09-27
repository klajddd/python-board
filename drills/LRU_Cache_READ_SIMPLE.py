
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.order = []

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            keyToRemove = self.order.pop(0)
            del self.cache[keyToRemove]
        self.cache[key] = value
        self.order.append(key)

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None

cache = LRUCache(3)
cache.put(1, 'one')
cache.put(2, 'two')
cache.put(3, 'three')
cache.put(4, 'four')

print(cache.get(1))
print(cache.get(2))

