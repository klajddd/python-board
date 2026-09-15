class Solution:
    def characterCount(self, inputString):
        charCountMap = {}
        strArray = list(inputString)
        for char in strArray:
            if char in charCountMap:
                charCountMap[char] += 1
            else:
                charCountMap[char] = 0
        return charCountMap


if __name__ == "__main__":
    s = Solution()
    print(s.characterCount('klajdkaraj'))
