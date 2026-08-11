import sys


class Solution:

    # time O(N)
    # space O(1)
    def best_time_to_buy_stock_best_answer(self, prices):

        if len(prices) < 2:
            raise ValueError('Producing profit requires 2 prices.')
        
        min_price = float('inf')
        
        max_profit = 0

        for i in range(len(prices)):
        
            current_price = prices[i]

            if current_price < min_price:
                min_price = current_price

            elif max_profit < current_price - min_price:
                max_profit = current_price - min_price
        
        return max_profit






    def bruteForceBestTimeToBuyStock(self, prices):

        max_profit = 0
        
        for earlierTime, earlierPrice in enumerate(prices):
        
            for laterTime in range(earlierTime+1, len(prices)):
        
                laterPrice = prices[laterTime]
        
                profit = laterPrice-earlierPrice
        
                max_profit = max(max_profit, profit)
        
        return max_profit


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
a = [1, 2, 3, 4, 50, 51, 0, 52, 53, 45, 46, 47] #53
b = [50, 49, 48, 45, 44, 43]


assert s.best_time_to_buy_stock_best_answer(a) == 53
assert s.best_time_to_buy_stock_best_answer(b) == 0

'''
BIG O

time complexity - O(n) linear

space complexity - O(1) constant,,,we only use flat probabilities in this example => best_profit, lowest & profit
'''
