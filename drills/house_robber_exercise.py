class Solution:


    # BOTTOM UP
    # TIME - O(n)
    # Space = O(1)
    def rob_bottom_up(self, nums: List[int]) -> int:
        
        if nums is None or len(nums) < 1:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
            
        house_prev_prev = nums[0]
        house_prev = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            next_house = max(nums[i] + house_prev_prev, house_prev)
            house_prev_prev = house_prev
            house_prev = next_house
            
        return house_prev


    # MEMOIZATION 
    # TIME - O(n)
    # SPACE - O(n)
    def rob(self, nums: List[int]) -> int:
        
        if nums is None or len(nums) < 1:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        
        memo = [-1] * len(nums)
        
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            memo[i] = max(memo[i-2] + nums[i], memo[i-1])
            
        return memo[-1]
