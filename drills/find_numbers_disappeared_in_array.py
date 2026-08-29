class Solution:
  # Time: O(n)
  # Space: O(1)
    def find_Disappeared_Numbers_negating(self, nums):
        return_list = []

        length = len(nums)

        for i in range(length):

            value = abs(nums[i]) - 1

            if nums[value] > 0:
                nums[value] *= -1

        for i in range(length):

            if nums[i] > 0:

                return_list.append(i+1)

        return return_list

  # Time: O(n)
  # Space: O(n)

    def findDisappearedNumbers(self, nums):
        return_list = []
        length = len(nums)
        nums_set = set(nums)

        for num in range(1, length+1):
            if num not in nums_set:
                return_list.append(num)

        return return_list


input = [4, 3, 2, 7, 8, 2, 3, 1]

s = Solution()

print(s.findDisappearedNumbers(input))

assert(s.find_Disappeared_Numbers_negating(input) == [5, 6])
