class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        left = 0
        right = 0

        for letter in s:
            if letter == 'L':
                left += 1
            else:
                right += 1
            if left == right:
                count += 1
        return count


s = Solution()

data = "RLRRLLRLRL"



import unittest
class TestSolution(unittest.TestCase):
    def testBalanced(self):
        self.assertEqual(s.balancedStringSplit(data), 4)


