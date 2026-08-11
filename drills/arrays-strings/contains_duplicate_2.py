import unittest

class Solution(object):

    # time: O(1)
    # space: O(min(n, k) where n is length of nums
    def containsNearbyDuplicate(self, nums, k):

        helper = {}

        for i in range(len(nums)):

            if nums[i] in helper:
                if i - helper[nums[i]] <= k:
                    return True
                else:
                    helper[nums[i]] = i
            else:
                helper[nums[i]] = i

        return False




class Test(unittest.TestCase):
    def test_contains_duplicate_2(self):
        s = Solution()
        result = s.containsNearbyDuplicate([1,2,3,1,2,3], 2)
        self.assertEqual(result, False)


if __name__=="__main__":
    unittest.main()




    '''
import unittest
class Test(unittest.TestCase):
    def test_three_meetings(self):
        s = Solution()
        self.assertEqual(s.minMeetingRooms([[0,30],[5,10],[15,20]]), 2, 'Should be 2 rooms.')

if __name__ == '__main__':
    unittest.main()
    '''

'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''