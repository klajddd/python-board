
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 0:
            return 0
        
        if n <= 1:
            return 1

        
        prev_prev  = 1
        prev = 1
        total_ways = 0
        
        for i in range(2, n+1):
            total_ways = prev_prev + prev
            prev_prev = prev 
            prev = total_ways
            
        return total_ways
            



        
        
        


        





# class Solution:
#     def climbStairs(self, n: int) -> int:
# # # #         DP = BOTTOM-UP APPROACH
# # # #         time: O(n), space O(1)=depth of the tree
#         if n < 0:
#             return 0
        
#         if n <= 1:
#             return 1

        
#         prev_prev  = 1
#         prev = 1
#         total_ways = 0
        
#         for i in range(2, n+1):
#             total_ways = prev_prev + prev
#             prev_prev = prev 
#             prev = total_ways
            
#         return total_ways

# # # #         MEMOIZATION = TOP-DOWN APPROACH
# # # #         time: O(n), space O(n)=depth of the tree
# #         memo = {}
# #         return self.climbStairsHelper(n, memo)
    
# #     def climbStairsHelper(self, n, memo):
# #         if n < 0:
# #             return 0
# #         elif n == 0:
# #             return 1
# #         elif n in memo:
# #             return memo[n]
# #         else:
# #             memo[n] = self.climbStairsHelper(n-1, memo) + self.climbStairsHelper(n-2, memo)
# #             return memo[n]
        
# # #         RECURSION
# # #         time: O(3^n), space O(n)=depth of the tree
# #         if n < 0:
# #             return 0
# #         elif n == 0:
# #             return 1
# #         else:
# #             return self.climbStairs(n-1) + self.climbStairs(n-2)
            
        
        
