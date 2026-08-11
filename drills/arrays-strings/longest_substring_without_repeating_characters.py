class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 1
        if len(s) < 1:
            return 0
        charMap = {s[0]:0}

        for i in range(1, len(s)):
            if s[i] in charMap and charMap[s[i]] >= start:
                start = charMap[s[i]] + 1
                charMap[s[i]] = i
            else:
                end = i
                charMap[s[i]] = i
                longest = max(longest, (end + 1 - start))

        return longest
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.validInput1 = "tmmzuxt"
    
    def testValidInput1(self):
        """Test valid input 1"""
        result = self.solution.lengthOfLongestSubstring(self.validInput1)
        self.assertEqual(5, result, 'Valid input 1 result should be: 5')
        
if __name__=="__main__":
    unittest.main()
        