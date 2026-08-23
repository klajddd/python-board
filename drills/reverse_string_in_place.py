class Solution:
    def __init__(self):
        pass

    def reverse_string(self, s):

        chars = list(s)

        for i in range(len(s) // 2):
            temp = chars[i]
            chars[i] = chars[len(s)-1-i]
            chars[len(s)-1-i] = temp

        return ''.join(chars)


s = Solution()
input = 'klajd'
assert s.reverse_string(input) == 'djalk'
