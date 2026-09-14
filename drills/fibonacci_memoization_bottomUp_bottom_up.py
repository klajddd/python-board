class Solution:

    def __init__(self):
        self.memo = {}

    def fibo(self, n):
        prev_prev = 0
        prev = 1

        for i in range(2, n):
            current = prev_prev + prev
            prev_prev = prev
            prev = current 
        return current






    # Time O(N)
    # Space O(1)
    def fibonacciBottomUp(self, n):
        if n < 0:
            raise IndexError("Index smaller than zero, not allowed.")
        if n <= 1:
            return n

        prevPrev = 0
        prev = 1

        for i in range(2, n + 1):
            current = prevPrev + prev
            prevPrev = prev
            prev = current

        return current




    # Time O(N)
    # Space O(N) the memo and the stack take N space each
    def fibonacciMemoization(self, n):
        if n < 0:
            raise IndexError("Sequence does not take a negative i.")

        if n <= 1:
            return n

        if n in self.memo:
            return self.memo[n]

        result = self.fibonacciMemoization(
            n-1) + self.fibonacciMemoization(n-2)

        self.memo[n] = result

        return result

    # Time O(2^n)
    # Space
    def fibonacciRecursion(self, n):
        if n < 0:
            raise IndexError("Sequence does not take a negative i.")

        if n <= 1:
            return n

        return self.fibonacciRecursion(n-1) + self.fibonacciRecursion(n-2)


s = Solution()
n = 600
print(s.fibonacciMemoization(n))
print(s.fibonacciBottomUp(n))
# print(s.fibonacciRecursion(n))
