class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena = len(a) - 1
        lenb = len(b) - 1
        result = []
        carry = 0
        while lena >= 0 or lenb >= 0:
            total = carry
            
            if lena >= 0:
                total += int(a[lena])
                lena -= 1
            
            if lenb >= 0:
                total += int(b[lenb])
                lenb -= 1
            
            carry = total // 2
            factor = total % 2
            result.append(str(factor))
        if carry == 1:
            result.append(str(carry))
        
        return "".join(reversed(result))


import unittest

class TestSolution(unittest.TestCase):
    def test_one(self):
        first = "11"
        second = "1"
        result = "100"
        s = Solution()
        self.assertEqual(s.addBinary(first, second), result)
        
if __name__ == "__main__":
    unittest.main()
        


        