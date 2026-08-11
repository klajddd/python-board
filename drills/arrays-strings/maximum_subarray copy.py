class Solution:
    # Time O(N)
    # Space O(1)
    # =============================== KADANE'S ALGORITHMS ======================================================
    def maxSubArray_efficient(self, nums):
        
        if len(nums) < 1:
            raise ValueError('nums list must contain at least 1 number')
        
        iterating_max_sub = nums[0]
        max_sub = nums[0]
        
        for i in range(1, len(nums)):

            current_value = nums[i]

            if current_value > iterating_max_sub + current_value:
                iterating_max_sub = current_value
            else:
                iterating_max_sub += current_value
                
            if iterating_max_sub > max_sub:
                max_sub = iterating_max_sub
                
        return max_sub

# =====================================================================================
    def maxSubArray_returns_zero(self, nums: 'List[int]') -> 'int':

        best_sum = 0
        current_sum = 0

        for x in nums:
            current_sum = max(0, current_sum + x)

            best_sum = max(best_sum, current_sum)

        return best_sum


  # BRUTE FORCE
  # time O(n^2), space O(1)
  # =====================================================================================
    def maxSubArray(self, nums):

        if len(nums) < 1:
            raise ValueError("list size is smaller than 1")
        
        max_sub = float('-inf')
        
        for i in range(len(nums)):
            
            current = 0            
            
            for j in range(i, len(nums)):
                
                current += nums[j]
                
                max_sub = max(max_sub, current)
            
        return max_sub





    def my_maxSubArray(self, nums: 'List[int]') -> 'int':
        
        if len(nums) < 1:
            raise ValueError("list size is smaller than 1")
        
        max_sub = float('-inf')
        
        for i in range(len(nums)):
            
            current = 0            
            
            for j in range(i, len(nums)):
                
                current += nums[j]
                
                max_sub = max(max_sub, current)
            
        return max_sub


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

input2 = [-2, 1]

input3 = [-52,-23,-38,-92,-69,-78,20,99,40,-5,-58,-8,-14,27,80,-10,41,77,64,-71,52,8,42,11,14,60,28,-77,
48,32,-72,72,86,-10,80,93,11,-23,69,-72,48,-88,19,-89,15,-23,-23,-67,-46,-58,-38,82,26,-96,-29,-83,40,98,-60,-12,31,-33,
-62,-6,33,94,-13,-79,-29,-43,-52,95]



s = Solution()

print(s.maxSubArray_efficient(input3))

assert s.maxSubArray_efficient(input3) == 806
