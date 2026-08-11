class Solution:

    # -----------------------------------------------------------------------
    # time O(n), space O(1)
    def is_palindrome_3(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
    # -----------------------------------------------------------------------


    def is_palindrome_2(self, string):
        reversed_string = ""
        for i in reversed(range(len(string))):
            reversed_string += string[i]

        return reversed_string == string

    # -----------------------------------------------------------------------

    def validPalindrome(self, s: str) -> bool:
        if self.checkForPalindrome(s):
            return True
        for i in range(len(s)):
            if self.checkForPalindrome(s[:i] + s[i + 1:]):
                return True
        return False

    def checkForPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    # -----------------------------------------------------------------------

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1

            elif not s[right].isalnum():
                right -= 1

            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True


    # -----------------------------------------------------------------------

    # time O(n), the mismatch runs only 1 time
    # space O(n), we make 2 additional lists before checking for is_palindrome

    def validPalindrome(self, string):
        start = 0
        end = len(string) - 1

        while start < end:
            if string[start] != string[end]:
                if self.is_palindrome(string[start + 1: end + 1]):
                    return True
                elif self.is_palindrome(string[start: end]):
                    return True
                else:
                    return False
            start += 1
            end -= 1

        return True

    def is_palindrome(self, s):
        chars = list(s)
        for i in range(len(s) // 2):
            if chars[i] != chars[len(chars) - 1 - i]:
                return False
        return True

    # -----------------------------------------------------------------------



if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
    assert s.validPalindrome("abaa") == True
