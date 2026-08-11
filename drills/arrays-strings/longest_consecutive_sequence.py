class Solution:
    # time: O(n)
    # space: O(n)
    def longestConsecutive(self, nums) -> int:
        setn = set(nums)

        result = 0
        seq = 0

        for el in setn:
            if (el-1) not in setn:
                seq = 1
                next = el + 1
                while next in setn:
                    seq += 1
                    next += 1
                result = max(result, seq)
                seq = 0
        return result
    
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        """Initialize a Solution instance before each test."""
        self.solution = Solution()
        
        # Valid list inputs
        self.nums1 = [100,4,200,1,3,2]
        self.nums2 = [0,3,7,2,5,8,4,6,0,1]
        
    
    def testFirstInput(self):
        """Test a valid input."""
        result = self.solution.longestConsecutive(self.nums1)
        self.assertEqual(result, 4, "Must be 4.")
        
        
    def testSecondInput(self):
        """Test a valid input."""
        result = self.solution.longestConsecutive(self.nums2)
        self.assertEqual(result, 9, "Must be 9.")

if __name__ == "__main__":
    unittest.main()
        
    