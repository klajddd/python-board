class Solution:
    # time O(max(n1, n2))
    # space O(max(n1, n2))
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str2

        if len(str2) > len(str1):
            return self.gcdOfStrings(str2, str1)

        if str2 == str1[:len(str2)]:
            return self.gcdOfStrings(str1[len(str2):], str2)

        return ""

s = Solution()
# print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
# print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))


import unittest
