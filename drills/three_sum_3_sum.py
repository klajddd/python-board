class Solution:
    # input with distinct input probabilities

    # time O(n^2)
    # space O(n)
    # [12, 3, 1, 2, -6, 5, -8, 6]
    #  ^   [                  ]
    def threeNumberSum_optimal(array, targetSum):
        # Write your code here.
        array.sort()
        triplets = []
        for i in range(len(array) - 2):
            left = i + 1
            right = len(array) - 1
            while left < right:
                currentSum = array[i] + array[left] + array[right]
                if currentSum == targetSum:
                    triplets.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
                elif currentSum > targetSum:
                    right -= 1
        return triplets


# ----------------------------------------------------------------------------------------------------------------------


    # time O(n^3)
    # space O(n)
    def three_sum(self, nums):

        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j+1, len(nums)):
                    
                    if nums[i] + nums[j] + nums[k] == 0:

                        min_val = min(nums[i], nums[j], nums[k])
                        max_val = max(nums[i], nums[j], nums[k])
                        
                        
                        mid_val = nums[i] + nums[j] + nums[k] - min_val - max_val

                        if [min_val, mid_val, max_val] not in result:
                            result.append([min_val, mid_val, max_val])

        return result



s = Solution()

in_arr = [-1,0,1,2,-1,-4]

print(s.three_sum(in_arr))