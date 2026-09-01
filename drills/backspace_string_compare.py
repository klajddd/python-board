# Time Complexity: O(M + N), where M, NM,N are the lengths of S and T respectively
# Space Complexity: O(M + N)


class Solution:
    def build(self, S):
        res = []
        for c in S:
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
        return "".join(res)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.build(S) == self.build(T)


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        pass


'''
"a#c"
"b"
'''
a = Solution()
print(a.backspaceCompare("a#c", "b"))
