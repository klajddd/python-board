'''

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to
    the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.

Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

import sys


class Solution:
    # time O(n)
    # space O(1)
    def pivotIndex_efficient(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

    # time O(n)
    # space O(n)
    def pivotIndex(self, nums):
        prefix = nums
        result = sys.maxsize
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        if prefix[0] == prefix[-1]:
            return 0

        if prefix[-2] == 0:
            result = len(prefix) - 1

        for i in range(1, len(prefix) - 1):
            if prefix[i - 1] == (prefix[-1] - prefix[i]):
                result = min(result, i)
        if result == sys.maxsize:
            return -1
        return result