class Solution:
    def generateParenthesis(self, n: int):
        
        result = []
        
        def recurse(open, close, iteration):
            if open == close == 0:
                result.append(iteration)
                return
            if open > 0:
                recurse(open - 1, close, iteration + "(")
            if close > open:
                recurse(open, close - 1, iteration + ")")
        recurse(n, n, "")
        print(result)
        return result

import unittest  # Import the unittest module

class TestSolution(unittest.TestCase):  # Define the test class

    def setUp(self):
        self.solution = Solution()  # Create an instance of the Solution class

    def test_generateParenthesis(self):
        self.assertEqual(self.solution.generateParenthesis(1), ["()"])  # Test case for n=1
        self.assertEqual(self.solution.generateParenthesis(2), ["(())", "()()"])  # Test case for n=2
        self.assertEqual(self.solution.generateParenthesis(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])  # Test case for n=3
        self.assertEqual(self.solution.generateParenthesis(0), [''])  # Test case for n=0


if __name__ == '__main__':
    unittest.main()




