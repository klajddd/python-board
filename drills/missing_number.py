class Solution:
    # Time O(n)
    # Space O(1)
    # Gauss formula
    def missing_number(self, nums) -> int:

        length = len(nums)

        total = (length) * ((length+1)//2)

        total_in_nums = 0

        for num in nums:

            total_in_nums += num

        return int(total - total_in_nums)

    # Time O(n)
    # Space O(1)
    # BIT MANIPULATION
    def missing_number_bit_manipulation(self, nums):

        missing = len(nums)

        for i, num in enumerate(nums):

            missing ^= i ^ num

        return missing


input = [1, 2, 3, 4]
s = Solution()
print(s.missing_numbe)
