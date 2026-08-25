class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # O(1) time
    def enqueue(self, item):
        self.in_stack.append(item)

    # O(1) time when out_stack not empty
    # We can get O(m) runtime for m calls.
    def dequeue(self):
        if len(self.out_stack) == 0:

            while len(self.in_stack) > 0:
                item = self.in_stack.pop()
                self.out_stack.append(item)

            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        return self.out_stack.pop()


