class Solution:

    # time O(n)
    # space O(1)
    def maxProfit(self, prices) -> int:
        total = 0
        localMin = prices[0]
        localMax = prices[0]
        for i in range(1, len(prices)):
            current = prices[i]
            if current < localMax:
                localMax = current
                localMin = current
            if current > localMax:
                localMax = current
                total += localMax-localMin
                localMin = localMax
        return total


    # time O(n)
    # space O(1)
    def maxProfit_compact_easier(self, prices) -> int:
        total = 0
        for i in range(1, len(prices)):
            current = prices[i]
            prev = prices[i-1]
            if current > prev:
                total += current - prev
        return total