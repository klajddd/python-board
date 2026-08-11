class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst = dict()
        mapts = dict()
        for i, el in enumerate(s):
            if el in mapst:
                if mapst[el] != t[i]:
                    return False
            else:
                mapst[el] = t[i]
            
            if t[i] in mapts:
                if mapts[t[i]] != el:
                    return False
            else:
                mapts[t[i]] = el
            
        return True
        

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        """Initialize a Solution instance before each test."""
        self.solution = Solution()
        self.s = "egg"
        self.t = "add"
        
        self.ss = "paper"
        self.tt = "title"
    
    def test_valid_strings(self):
        """Test solution for True."""
        result = self.solution.isIsomorphic(self.s, self.t)
        self.assertTrue(result, "Should return True")
    
    def test_invalid_string(self):
        """Test solution for True 2."""
        result = self.solution.isIsomorphic(self.ss, self.tt)
        self.assertTrue
        (result, "Should return False")
    


if __name__ == "__main__":
    unittest.main()
        


