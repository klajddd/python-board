'''
Find if nums array has duplicates
'''

class Solution:
    # time O(n log(n))
    # space O(1)
    def containsDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    # time O(n)
    # space O(n)
    def containsDuplicate(self, nums) -> bool:
        nums_dict = set()
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict.add(num)
        return False


input = [1, 2, 3, 1]
s = Solution()
print(s.containsDuplicate2(input))
