from typing import List
import string

# time: O(n)
# space: O(1)
class Solution():
    def singleNumber(self, nums):

        result = 0

        for element in nums:
            # XOR - changes numbers to binary
            result ^= element

        return result


s = Solution()
result = s.singleNumber([2, 3, 4, 3, 4, 2, 6, 7, 7])
print(result)

