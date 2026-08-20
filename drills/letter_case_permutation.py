import sys


class Solution:

    # time O(N)
    # space O(1)
    def bestTimeToBuyStockBestAnswer(self, prices):
        if len(prices) < 2:
            raise ValueError('Producing profit requires 2 prices.')
        minPrice = prices[0]
        maxProfit = prices[1] - prices[0]
        for i in range(1, len(prices)):
            currentPrice = prices[i]
            profit = currentPrice - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, currentPrice)
        return maxProfit


    def bruteForceBestTimeToBuyStock(self, prices):
        maxProfit = 0
        for earlierTime, earlierPrice in enumerate(prices):
            for laterTime in range(earlierTime+1, len(prices)):
                laterPrice = prices[laterTime]
                profit = laterPrice-earlierPrice
                maxProfit = max(maxProfit, profit)
        return maxProfit


    def bestTimeToBuyStock(self, prices):
        bestProfit = 0
        lowest = float('inf')

        for price in prices:
            profit = price - lowest
            if profit > bestProfit:
                bestProfit = profit
            if price < lowest:
                lowest = price
        return bestProfit


s = Solution()
a = [1, 2, 3, 4, 50, 51, 0, 52, 53, 45, 46, 47]
b = [50, 49, 48, 45, 44, 43]
print('best profit is {}'.format(s.bestTimeToBuyStock(a)))

print('best profit is {}'.format(s.bruteForceBestTimeToBuyStock(a)))

print('best profit is {}'.format(s.bestTimeToBuyStockBestAnswer(a)))


# print('profit is {} = {} - {}'.format(best_profit, lowest+best_profit, lowest))

'''
BIG O

time complexity - O(n) linear

space complexity - O(1) constant,,,we only use flat probabilities in this example => best_profit, lowest & profit
'''
