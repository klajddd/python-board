import traceback
import time

"""
array child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

s - - - - - - - - - - e
                ^
tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)

"""


class Solution:

    def recursionCountWays(self, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.recursionCountWays(n - 1) + self.recursionCountWays(n - 2) + self.recursionCountWays(n - 3)

    def memoizationCountWays(self, n):
        memo = [-1] * (n+1)
        return self.memoizationCountWaysHelper(n, memo)

    def memoizationCountWaysHelper(self, n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if memo[n] > -1:
                return memo[n]
            else:
                memo[n] = self.memoizationCountWaysHelper(
                    n-1, memo) + self.memoizationCountWaysHelper(n-2, memo) + self.memoizationCountWaysHelper(n-3, memo)
                return memo[n]


n = 18
s = Solution()
start0 = time.time()
print(s.recursionCountWays(n))
end0 = time.time()
print(end0-start0)

start = time.time()
print(s.memoizationCountWays(n))
end = time.time()
print(end-start)
