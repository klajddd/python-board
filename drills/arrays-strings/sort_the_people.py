class Solution:
    def sortPeople(self, names, heights):
        d = dict(zip(heights, names))
        sortedHeights = sorted(heights, reverse=True)
        sortedNames = []
        for el in sortedHeights:
            sortedNames.append(d[el])
        return sortedNames

import unittest
from typing import List

class TestSolution(unittest.TestCase):
    def setUp(self):
        """Initialize a Solution instance before each test."""
        self.solution = Solution()
    
    def test_basic_case(self):
        """Test with a simple case of three people."""
        names = ["Mary", "John", "Emma"]
        heights = [180, 165, 170]
        expected = ["Mary", "Emma", "John"]
        result = self.solution.sortPeople(names, heights)
        self.assertEqual(result, expected, "Should sort people by height in descending order")
    
    def test_single_person(self):
        """Test with a single person."""
        names = ["Solo"]
        heights = [175]
        expected = ["Solo"]
        result = self.solution.sortPeople(names, heights)
        self.assertEqual(result, expected, "Should work with a single person")
    
    def test_reverse_sorted(self):
        """Test with input sorted in reverse order."""
        names = ["Short", "Medium", "Tall"]
        heights = [160, 175, 190]
        expected = ["Tall", "Medium", "Short"]
        result = self.solution.sortPeople(names, heights)
        self.assertEqual(result, expected, "Should reverse order when input is reverse sorted")

if __name__ == "__main__":
    unittest.main()
