'''
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. 
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
'''


class Solution:
    def minPartitions(self, n: str) -> int:
      maxx = 0
      for ch in n:
        maxx = max(maxx, int(ch))
      return maxx


import unittest

class TestSolution(unittest.TestCase):
    def testMainCase(self):
        s = Solution()
        result = s.minPartitions('32')
        self.assertEqual(result, 3, 'Numbers are not the same')


if __name__ == "__main__":
    unittest.main()
