class Solution:

    #     time: O(n)
    #     space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        left, right, longest = 0, 0, 0

        substring = set()

        while right < len(s):
            char = s[right]
            if char not in substring:
                substring.add(char)
                right += 1
                longest = max(longest, len(substring))
            else:
                substring.remove(s[left])
                left += 1

        return longest

#     time: O(n^2)
#     space: O(n)

    def lengthOfLongestSubstring_brute_force(self, s: str) -> int:

        if len(s) < 1:
            return 0

        longest = 0
        result = 0

        chars_set = set()

        for i in range(len(s)):
            chars_set = set()
            longest = 0
            for j in range(i, len(s)):
                if s[j] in chars_set:
                    break
                else:
                    chars_set.add(s[j])
                    longest += 1
            if longest > result:
                result = longest

        return result
