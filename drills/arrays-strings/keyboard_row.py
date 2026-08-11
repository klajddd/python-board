from typing import List
import unittest

class Solution:
    # time: O(n) where n is length of words
    # space: O(n)
    def findWords(self, words: List[str]) -> List[str]:
        result = []
         
        firstRow = 'qwertyuiop'
        secondRow = 'asdfghjkl'
        thirdRow = 'zxcvbnm'

        for word in words:
            if len(set(firstRow + word.lower())) == len(firstRow) or len(set(secondRow + word.lower())) == len(secondRow) or len(set(thirdRow + word.lower())) == len(thirdRow):
                result.append(word)


        return result
    
    

class TestSolution(unittest.TestCase):
    def testFindWords(self):
        words = ["Hello", "Alaska", "Dad", "Peace"]
        s = Solution()
        self.assertEqual(s.findWords(words), ["Alaska", "Dad"])


if __name__ == "__main__":
    unittest.main()