class Solution:
    # O(n) time
    # O(1) space
    def longestCommonPrefix_efficient(self, strs) -> str:

        min_word = min(strs, key=len)

        for i in range(len(min_word)):

            for word in strs:
                if word[i] is min_word[i]:
                    continue
                else:

                    return min_word[:i]

        return min_word




    def longestCommonPrefix(self, strs) -> str:

        result = []

        min_word = min(strs, key=len)

        for i in range(len(min_word)):

            result.append(min_word[i])
            for word in strs:
                if word[i] is result[-1]:
                    continue
                else:

                    result[-1] = ""
                    return "".join(result)

        return "".join(result)

s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["cir","car"]))