'''
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options.
For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'.
The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.

Input: s = "{a,b}c{d,e}f"
Output: ['acdf', 'acef', 'bcdf', 'bcef']

Input: s = "abcd"
Output: ['abcd']
'''

class Solution:
    def expand(self, S: str):

        self.result = []

        self._expand(S, 0, len(S), "")

        return sorted(self.result)


    def _expand(self, string: str, start: int, size: int, prefix: str):
        if start == size:
            self.result.append(prefix)
            return

        if string[start] == "{":

            end = string.find("}", start)

            for letter in string[start + 1: end].split(","):
                self._expand(string, end + 1, size, prefix + letter)

        else:
            self._expand(string, start + 1, size, prefix + string[start])


import unittest
class TestExpand(unittest.TestCase):

    def test_string(self):
        sol = Solution()
        s = "{a,b}c{d,e}f"
        print(sol.expand(s))
        self.assertEqual(sol.expand(s), ['acdf', 'acef', 'bcdf', 'bcef'], 'Failed')

if __name__=='__main__':
    unittest.main()
