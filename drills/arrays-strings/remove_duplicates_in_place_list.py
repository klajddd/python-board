from typing import List

class Solution:
# ====================================================================== 
    def removeDuplicates_efficient(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1

# ====================================================================== 
    
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                nums[i] = None
                k += 1
            else:
                seen.add(nums[i])

        first = 1
        second = 0

        while first < len(nums):
            if nums[second] is None:
                if nums[first] is not None:
                    nums[first], nums[second] = nums[second], nums[first]
                    second += 1
            else:
                second += 1
            
            first += 1
        print(f'list is -> {nums}')
        return k
    

l = [0,0,1,1,1,2,2,3,3,4]
val = 2
s = Solution()
print(s.removeDuplicates_efficient(l))