class Solution:

    def maxSubarraySumCircular(self, nums):

        total = 0

        max_sum = nums[0]

        current_max = 0

        min_sum = nums[0]

        current_min = 0

        for current_num in nums:

            current_max = max(current_num + current_max, current_num)
            max_sum = max(max_sum, current_max)

            current_min = min(current_num + current_min, current_num)
            min_sum = min(min_sum, current_min)

            total += current_num

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum

s = Solution()

print(s.maxSubarraySumCircular([1,-2,3,-2]))