'''
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
'''

# O(n) space
# O(n) time
class Solution:
    def shuffle(self, nums, n: int):
        result_arr = [None] * len(nums)

        for i in range(0, n):
            result_arr[2 * i] = nums[i]
            result_arr[2 * i + 1] = nums[i + n]

        return result_arr

# O(1) space
# O(n) time

    '''
    Each "nums[i]" has a "desired" i.
    e.g. for an array of 8 numbers, nums[0] wants to go to i "0", nums[4] wants to go to i "1", nums[1] wants to go to i "2", nums[5] wants to go to i "3", nums[2] wants to go to i "4"...
    The target i of nums[i] is nums[i]'s "desired i".
    We loop through all nums and swap each nums[i] into its "desired" i. As soon as a number is placed into its "desired" place, we mark it as "negative", so that it won't be processed again when we see it later (yes, because nums[i]'s desired i might be after itself, we might see it agian later).
    Now nums[i] is in its desired place, but how about another number that "is swapped" by nums[i]? That number is currently in position "i" now because of the swap. We recursively put that number into its "desired" place too, until all the "be-swapped" numbers are also in their desired place.
    After that, we can move to the next i "i" and do the same thing.
    Don't forget to change all numbers back to positive value after all finsihed.
    '''
    def shuffle_1_space_n_time(self, nums, n: int):
        getDesireIdx = lambda i: i*2 if i<n else (i-n)*2+1
        for i in range(2*n):
            j=i
            while nums[i] >= 0:
                j = getDesireIdx(j)
                nums[i], nums[j] = nums[j], -nums[i]
        for i in range(2*n):
            nums[i] =- nums[i]
        return nums



import unittest

class TestClass(unittest.TestCase):
    def test_array(self):
        s = Solution()
        self.assertEqual(s.shuffle([1, 2, 3, 4, 5, 6, 7, 8], 4), [1, 5, 2, 6, 3, 7, 4, 8], 'Test array failed')

if __name__ == "__main__":
    unittest.main()